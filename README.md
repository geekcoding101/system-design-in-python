# System Design in Python

This repository contains Python code implementations of system design concepts inspired by the book **Designing Data-Intensive Applications** by Martin Kleppmann. The goal is to help learners and practitioners explore key principles in system design through practical Python examples.

## Concepts Covered

This repository includes Python implementations of various data systems concepts discussed in the book, including but not limited to:

- **Data Modeling**: Modeling data using the appropriate techniques (e.g., normalization, denormalization).
- **Consistency & Availability**: Implementing basic concepts of CAP theorem and consistency models.
- **Sharding**: Implementing database sharding techniques to scale horizontally.
- **Replication**: Simulating data replication for fault tolerance and availability.
- **Batch vs. Stream Processing**: Exploring the differences and use cases of batch processing and stream processing.
- **Eventual Consistency**: Implementing systems that ensure eventual consistency in distributed databases.
- **Distributed Transactions**: Exploring methods for handling distributed transactions.
- **Message Queues & Kafka**: Building message queues and simulating systems like Apache Kafka.

## Prerequisites

- Python 3.x
- Familiarity with the concepts from the book *Designing Data-Intensive Applications*
- A basic understanding of system design and distributed systems

## Setup

To get started, clone the repository:

```
git clone https://github.com/your-username/System-Design-in-Python.git
```

Navigate to the repository:

```
cd System-Design-in-Python
```

Ensure Python 3.x is installed on your system.

## Example Concepts and Implementations

Each concept is implemented in its own directory. Below are the key examples you'll find in this repository.

### 1. **Data Modeling**

This directory contains Python scripts to demonstrate data modeling techniques.

- **Normalization**: Breaking down tables to reduce redundancy.
- **Denormalization**: Combining data for performance optimization.

```
python data_modeling.py
```

### 2. **Sharding**

Sharding is a technique for distributing data across multiple databases. This example demonstrates how data can be partitioned horizontally.

```
python sharding.py
```

### 3. **Replication**

This directory demonstrates how data replication works in distributed systems, ensuring fault tolerance and high availability.

```
python replication.py
```

### 4. **Batch vs. Stream Processing**

Learn the difference between batch processing (processing large chunks of data) and stream processing (real-time data processing).

- **Batch Processing**: Examples of batch jobs.
- **Stream Processing**: Using tools like Kafka and Python to simulate stream processing.

```
python batch_processing.py
python stream_processing.py
```

### 5. **Eventual Consistency**

This directory shows how systems can be eventually consistent, meaning that updates propagate across all systems over time.

```
python eventual_consistency.py
```

### 6. **Distributed Transactions**

Implementing a system to handle distributed transactions with concepts like 2-phase commit.

```
python distributed_transactions.py
```

### 7. **Message Queues (e.g., Kafka)**

Simulate message queues for building decoupled and resilient systems. This directory covers message queues like Apache Kafka.

```
python message_queue.py
```

## Usage

To run any example, simply execute the corresponding Python script. For example, for the sharding example, run:

```
python sharding.py
```

## Contributing

Contributions are always welcome! If you have an idea for improving the repository or adding new concepts, feel free to fork the repository, create a new branch, and submit a pull request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
