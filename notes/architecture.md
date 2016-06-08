# Overview of computer architecture

Why: architecture affects speed of your program, primarily memory hierarchy. (Algorithm is biggest but not arch issue)

Draw CPU, RAM, disk, bus interconnect

RAM holds both the program and any data needed by the program. The memory also holds the operating system which manages the execution of processes and the physical devices.  RAM is a set of addressable pigeonholes from 0..N for N=maybe 8G in your laptop, which is 8,000M or 8,000,000k or 8,000,000,000 bytes or 8 billion bytes. That the lot. The San Francisco phonebook is maybe 10 MB.

Random-access.

RAM is typically much smaller than the disk storage size.

volatile: memory disappears when you turn the computer off.

Bit vs byte. bit (BInary digiT) is the smallest unit of information in a computer. yes/no, 0/1. M/F.

You should get familiar with k, M, G for memory size requirements to know how much your program requires for operation or how big a disk file will be.

CPU execs very simple instructions (arith, compare, jump, ...) but very quickly

mov r0, 5		; r0 = 5
mov r1, 10	; r1 = 10
add r2, r0, r1; r2 = r0 + r1

CPUs execute instructions to the heartbeat of a clock, which is where we get the term clock rate. For example, a 1Ghz clock such as you might have on your phone, gives 1 billion tics per second. That means each instruction takes 1 billionth of a second or 1 nanosecond. It goes milli, micro, nano, femto

Many instructions can operate in just one clock cycle, but some take several... particularly if it has to go to RAM.

Draw GPU on bus

Draw network card with network connection

Network transfer speeds. You are limited to say 10Mbps on USF connections but I have 100 Mb per second at home. the University has a number of 1G channels. how long does it take to transfer a 1G file?

the physical layer is called ethernet but there are lots of different kinds of networks. Ethernet is 10-1000M bits / sec

Wireless is another physical layer that uses radio waves to transmit information. This is like the electrical connection/wires used by ethernet.