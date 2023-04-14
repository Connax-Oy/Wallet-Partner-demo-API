## VPC
- Create or use default VPC with local region subnets

## MemoryDB Redis cache

- Create new MemoryDB cluster
- Choose the VPC and its subnets
- Choose the default security group.
- Encryption in transit disabled. ACL open-access.

## Security group
Add inbound permission: Custom TCP Port `6379` (MemoryDB port) source `0.0.0.0/0`

## Lambda

- Create Lambda function.
- Configure with the VPC and the same default security group.
- In the source code, edit `src/config.py` with MemoryDB host and port

The following steps depend on the method of uploading
code to the Lambda function.

### Complete deployment package

- Create deployment package with Redis dependencies:
```
pip install --target=./package/ redis
cd package
zip -r ../deployment_package.zip .
cd ../src
zip ../deployment_package.zip lambda_function.py config.py
cd ..
```

- Upload deployment_package.zip

**or**

### Upload source code and add Redis Lambda layer

- Download redis and its dependencies locally
and add it to a .zip archive. Dependencies should
be located inside `python/` directory.

```
pip install --target=./redis/python/ redis
cd redis
zip -r ../redis.zip .
cd ..
```

- Upload this .zip archive as a layer **redis**.
- Create a .zip archive with the source code files:
```
cd src
zip -r ../lambda.zip .
cd ..
```
- Upload the source code to the Lambda function.
- Add **redis** layer to the Lambda function