# Overview of computer architecture

Why: architecture affects speed of your program, primarily CPU, memory hierarchy, network. (Algorithm is biggest but not arch issue) how big of a data set can you process? How fast can you transfer data beween machines? You should know the terminology used in the computing field, even if it's just for passing interviews.

get motherboard image, such as [motherboard](https://pixabay.com/en/technology-computer-motherboard-1396677/)

![](figures/motherboard.jpg)

Conceptual integrity or theme: everything is a network of computing, storage, input device, display device. At all layers we will see the same fractal pattern.

Draw CPU, RAM, USB bus with mouse/keyboard, disk, bus interconnect.

[Basic architecture](figures/arch0.pdf)

## Memory

RAM [image](https://pixabay.com/en/computer-memory-chips-technology-857098/) (note 8 chips on package) 

* holds both the program and any data needed by the program.
* The memory also holds the operating system which manages the execution of processes and the physical devices.
* RAM is a set of addressable pigeonholes from 0..N-1
* Each pigeonhole or cell is a byte == 8 bits
* Bit vs byte. bit (BInary digiT) is the smallest unit of information in a computer. yes/no, 0/1. M/F.
* For N=maybe 8G in your laptop, which is 8,000M or 8,000,000K or 8,000,000,000 bytes or 8 billion bytes. That's a lot. The San Francisco phonebook is maybe 8 MB.

Q. How many 8M phonebooks could your 8G laptop hold in RAM? 8000M/8M = 1000 books.

Random-access vs tape storage, which is serial. A network is also serial as we will see: it transmits one bit at a time by wiggling current on a wire.

RAM is typically much smaller than the disk storage size but much faster.

DRAM is volatile: memory disappears when you turn the computer off. this is the biggest chunk of RAM you have.

ROM: firmware, which holds basic code to boot up the computer and manage the lowest level connection to devices.

Static RAM "flash memory": SD cards. e.g., phone pic/data storage.  nonvolatile but slower.

You should get familiar with k, M, G, T for memory size requirements to know how much your program requires for operation or how big a disk file will be. (note that 1000 is also used instead of 1024)

|value | units |
|------|-------|
1024	| kB	kilobyte (2^10)
1024^2	| MB	megabyte
1024^3	| GB	gigabyte
1024^4	| TB	terabyte

Q. How many bytes is 4k?

Q. How many k in a M? G?

Q. What is stored in RAM?

Q. What does the operative system do?

## CPU

CPU execs very simple instructions (arith, compare, jump, ...) but very quickly. e.g.,

```
mov r0, 5		; r0 = 5
mov r1, 10	; r1 = 10
add r2, r0, r1; r2 = r0 + r1
```

r0-r32 are like a fixed size set of temporary variables called *registers*. All operations take place in these suckers.

CPUs execute instructions to the heartbeat of a clock, which is where we get the term clock rate. Mhz (million herz==cycles/second), Ghz (billion) are the typically units in clock ticks per second. Why cycles? because the clock is actually a square wave, jumping from zero to about +5V and back down.  On the rising edge of the wave, we get a tick.

*Example*: a 1Ghz clock such as you might have on your phone, gives 1 billion ticks per second. That means each instruction takes 1 billionth of a second or 1 nanosecond. Units go milli, micro, nano, femto.

Q. How long is a nanosecond? I.e., how far can light go in a nanosecond? 11.8" long for 1 billionth of a second. 1us = 984'

<a href="https://youtu.be/JEpsKnWZrJ8">Grace Hopper on a nanosecond</a>.

**Units or your guide!**

Clock tick duration: 1 / herz = 1 / ticks-per-second = duration in seconds

Duration in seconds for n tick: n / ticks-per-second = duration in seconds

Number of ticks in n seconds: ticks-per-second * n sec = ticks


Q. How many ticks / sec with a 1Mhz clock? 4Mhz? 1 million per second and 4 million per second.

Q. How many multiplies (at 1 tick-per-multiply) can a 1Mhz CPU do in 1 second? 1 million to ask for second * 1 sec = 1 million multiplies.

Q. How many multiplies can a 4Ghz CPU do in 3 second? 4 billion instructions per second * 3 seconds = 12 billion instructions.

Q. How long will it take to do 1000 multiplies on a 1 MHz processor? 1000 instructions / 1 million instructions per second = 1 / 1000 = 0.001 = 1ms.

Many instructions can operate in just one clock cycle, but some take several... particularly if it has to go to RAM.

Count to 10,000,000 takes about a second (wow)

```python
for i in range(10000000): pass
```

Count to 100,000,000 takes about 5 seconds

```python
for i in range(100000000): pass
```

Example: My Mac's clock rate is 4Ghz, which means 4 billion clock ticks / second. That loop takes 5 seconds so does 5 * 4,000,000,000 ticks = 20 billion ticks. For 100,000,000 iterations, that is 200 ticks per iteration.  In C, that loop takes about 0.2s. To do 10x as many iterations, takes about 2.2s.

### Moore's law and transistor count

Transistor count doubles every 2 years but people mistake it for clock rate doubling.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Transistor_Count_and_Moore%27s_Law_-_2011.svg/800px-Transistor_Count_and_Moore%27s_Law_-_2011.svg.png" width=500>

We're just about at the physical limit in size (due to quantum tunneling affects) and speed (due to heat dissipation issues).  E.g., we have a compute node here that is liquid cooled.

<img src=figures/liquid-cooling.jpg width=400>

We're using real estate to make more processors, hoping to get speed boost through parallel processing. Draw another processor on bus [Multiple-CPU](figures/arch1.pdf)

GPU is just another processor on the bus with its own memory.

Nowadays we have lots of room on chip so we pack in more core: [Core](figures/core.pdf)

### Cache

CPUs have gotten faster much more quickly than memory speed, which is a serious bottleneck.

![speed of CPU versus RAM over time](http://www.extremetech.com/wp-content/uploads/2014/08/CPU-DRAM.png)
 
ARM assembly to load byte data at address 100 into register.

```
MOV r3, 100    ; 1 ns
LDR r4, [r3]   ; 80-120ns
```

Draw caches between processor and bus: [Multi-CPU, RAM banks, cache](figures/arch2.pdf)

The processor runs many many times faster than the memory so we created faster but smaller RAM that can hold frequently accessed data closer to the processor. There can be three levels of cache and then within the processor there is the register set which is superfast but very limited in size.

* L1 cache might have a 1ns access latency. size 64k code/16k data
* L2 10ns latency. 2MB
* L3 ~85ns latency 8M

There is a memory hierarchy that gets slower and slower as you go outwards. We can even view the RAM on other machines as part of our network.

## Networks

Draw network card with network connection

Unit of transfer at the physical layer is one bit, usually wiggling current on a single wire. Logically, however, we think of transferring data in chunks called packets of a specific size. Files are broken down into multiple packets and transmitted over the network. (More and data acquisition class.)

There are two critical measurements:

* latency: how long it takes to get the first bit to/from the remote node. This is how long it takes before you start seeing a webpage.
* throughput: how many bits per second you can transmit once a connection is established. This is how long it takes before the entire webpage comes across (browser finishes displaying it).

[Basic network](figures/network.pdf)

Network transfer speeds usually measured in *bps*=bits per second. *Bps* usually means bytes per second. A byte is 8 bits.

* You are limited to say 10Mbps on USF connections 
* I have 100 Mbps per second at home.
* The University has a number of 1Gbps "gigabit" channels. 

The units spell out the relationship:

*size in bits* / *speed in bits per second* = *duration in seconds*

1. Convert file size to bits from bytes.
2. Convert network speed to bits per second
3. Divide to get duration in seconds

Or, use bigger units

1. Convert file size to bits from bytes; divide by 1 million to get megabits
2. Convert network speed to bits per second; divide by 1 million to get megabits per second
3. Divide to get duration in seconds

Q. How long does it take to transfer a 1M file across a 8Mbps channel? (Remember 1M means 1M * 8 bits) We can transmit entire 8 million bits of the file in 1 second on an 8Mbps channel.
Q. How long does it take to transfer a 10M file across a 8Mbps channel? 80 Mb / 8 Mbps = 10 s.
Q. How long does it take to transfer a 1G file across a 1Mbps channel? 8000Mb / 1Mb = 8000s = 133.3 minutes = 2.2 hours

the physical layer is called ethernet but there are lots of different kinds of networks. Ethernet is 10-1000M bits / sec

Wireless is another physical layer that uses radio waves to transmit information. This is like the electrical connection/wires used by ethernet.

## Cloud Computing

[Clould computing](figures/arch3.pdf)