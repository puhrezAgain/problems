package main

import (
	"errors"
	"fmt"
)

type PaymentStore struct {
	// TODO
	orders []string
}

var ErrAlreadyCharged = errors.New("already charged")

func NewPaymentStore() *PaymentStore {
	return &PaymentStore{}
}

func (ps *PaymentStore) Charge(orderID string) error {
	// TODO
	for _, o := range ps.orders {
		if o == orderID {
			return ErrAlreadyCharged
		}
	}
	ps.orders = append(ps.orders, orderID)
	return nil
}

func main1() {
	ps := NewPaymentStore()

	for i := 0; i < 3; i++ {
		err := ps.Charge("order-123")
		fmt.Println("attempt", i, "err:", err)
	}
}
