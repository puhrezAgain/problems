package main

import (
	"context"
	"fmt"
)

func worker(ctx context.Context, jobs <-chan int, results chan<- int) {
	// TODO
	for {
		select {
		case input := <-jobs:
			results <- input * input
		case <-ctx.Done():
			close(results)
			return
		}
	}

}

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	jobs := make(chan int)
	results := make(chan int)

	go worker(ctx, jobs, results)

	go func() {
		for i := 1; i <= 5; i++ {
			jobs <- i
		}
		cancel()
		close(jobs)
	}()

	for r := range results {
		fmt.Println(r)
	}
}
