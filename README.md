# gRPC and protocol buffers

Introduction

This is a client server implementation using gRPC for serialization and transport.

gRPC basics

- uses [Protocol Buffers](https://developers.google.com/protocol-buffers) for serialization. This means that your data structure is encoded into bytes and ready for transport
- uses [http2](HTTP2) tcp protocol for transport which guarantees delivery

Services

- `Go` service which will collect metrics (dummy)
- `Python` service which will detect the anomaly

The `Go` client will communicate with the `Python` server via [gRPC](https://grpc.io/)

In `gRPC` we define a proto file in which we define the messages which get sent and RPC methods. Our method `Detect` uses an `OutliersRequest` message type as the input and an `OutliersResponse` message type for the output. The OutliersRequest message type is a list/slice of Metric and the OutliersResponse message type is a list/slice of indices where the outlier values were found.

## Instructions to run

- create a virtualenv `python3 -m venv venv`
- Activate it `source venv/bin/activate`
- Install the python requirements of numpy and grpcio-tools package`python -m pip install -r py/requirements.txt`
- Generate the server gRPC files

    ```bash

    python -m grpc_tools.protoc -I..--python_out=. --grpc_python_out=. ../outliers.proto
    ```

- Include GO envars in PATH
- `export PATH=$PATH:/usr/local/go/bin`
- `export PATH=$PATH:$HOME/go/bin`
- Install protobuf to generate GO gRPC files
- `go get github.com/golang/protobuf/protoc-gen-go`
- `go generate`
- `python server.py` in one terminal and `go run client.go` in another