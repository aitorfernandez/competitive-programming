package main

import (
	"reflect"
	"testing"
)

var tests = []struct {
	table  []row
	column string
	output row
}{
	{[]row{{"a": 1}, {"a": 2}, {"a": 3}}, "a", row{"a": 1}},
	{[]row{{"a": 1, "b": 2}, {"a": 3, "b": 0}}, "b", row{"a": 3, "b": 0}},
	{[]row{{"a": 1, "b": -2}, {"a": 3}}, "b", row{"a": 3, "b": -2}},
}

func TestMinByColumn(t *testing.T) {
	for _, test := range tests {
		got := minByColumn(test.table, test.column)

		if !reflect.DeepEqual(got, test.output) {
			t.Errorf("got %v, want %v", got, test.output)
		}
	}
}
