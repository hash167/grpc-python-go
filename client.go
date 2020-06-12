package main

import (
	"context"
	"grpc_test/pb"
	"log"
	"math/rand"
	"time"

	"google.golang.org/grpc"
	pbtime "google.golang.org/protobuf/types/known/timestamppb"
)

func main() {
	addr := "localhost:9999"
	conn, err := grpc.Dial(addr, grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()

	client := pb.NewOutliersClient(conn)
	req := pb.OutliersRequest{
		Metrics: dummyData(),
	}
	resp, err := client.Detect(context.Background(), &req)

	if err != nil {
		log.Fatal(err)
	}
	log.Printf("outliers at: %v ", resp.Indices)
}

func dummyData() []*pb.Metric {
	const size = 1000
	out := make([]*pb.Metric, size)
	t := time.Date(2020, 5, 22, 14, 13, 11, 0, time.UTC)
	for i := 0; i < size; i++ {
		m := &pb.Metric{
			Time: Timestamp(t),
			Name: "CPU",
			// Normally below 40 % CPU ultilization
			Value: rand.Float64() * 40,
		}
		out[i] = m
		t.Add(time.Second)
	}

	// Create outliers
	out[9].Value = 99.3
	out[343].Value = 98.12
	out[999].Value = 87.10
	return out
}

// Timestamp converts time.Time to protobuf *Timestamp
func Timestamp(t time.Time) *pbtime.Timestamp {
	return &pbtime.Timestamp{
		Seconds: t.Unix(),
		Nanos:   int32(t.Nanosecond()),
	}
}
