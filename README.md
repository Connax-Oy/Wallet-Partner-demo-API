# Wallet-Partner-demo-API
Example of partner side API for Wallet Pass

This example is an AWS Lambda function interface
meant to interact with a Redis cache.

## API specification

This example follows [these specifications](doc/api-specification.md) for Partner API.

## Source code

Located in the `src/` directory.

Expects invocation with REST request, but can be tested with direct Lambda function invocation.

Uses RedisCluster to connect to MemoryDB Redis cache because of MemoryDB specifics.

## Setup

You can find more in-depth setup instructions [in here](doc/setup.md).

Note: Edit `src/config.py` with your Redis cache host and port.

Note: You will have to add Redis python library to the function.