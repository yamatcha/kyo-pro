DIR := $(shell pwd)
a: $(DIR)/A/main.go
	docker run -w /go/src -it --rm -v $(DIR)/A:/go/src golang:1.6 go run main.go
b: $(DIR)/B/main.go
	docker run -w /go/src -it --rm -v $(DIR)/B:/go/src golang:1.6 go run main.go
c: $(DIR)/C/main.go
	docker run -w /go/src -it --rm -v $(DIR)/C:/go/src golang:1.6  go run main.go
d: $(DIR)/D/main.go
	docker run -w /go/src -it --rm -v $(DIR)/D:/go/src golang:1.6 go run main.go
