## VPC
- Create or use default VPC with local region subnets

## MemoryDB Redis cache

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
zip -r ../deployment_package.zip
cd ..
zip deployment_package.zip src/lambda_function.py src/config.py
```

- Upload deployment_package.zip

**or**

### Upload source code and add Redis Lambda layer

- Download redis and its dependencies locally
and add it to a .zip archive. Dependencies should
be located inside `python/` directory.

```
pip install --target=./redis/python/ redis
zip -r redis.zip redis
```

- Upload this .zip archive as a layer **redis**.
- Create a .zip archive with the source code:
```
zip -r lambda.zip src
```
- Upload the source code to the Lambda function.
- Add **redis** layer to the Lambda function