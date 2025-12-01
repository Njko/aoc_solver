# Advent of Code 2015 Solutions Walkthrough

This document outlines the strategies used to solve the Advent of Code 2015 puzzles.

## Day 01: Not Quite Lisp
- **Part 1**: Count `(` as +1 and `)` as -1 to find the final floor.
- **Part 2**: Iterate and track the running sum. Return the index (1-based) where the sum first becomes -1.

## Day 02: I Was Told There Would Be No Math
- **Part 1**: Calculate surface area `2*l*w + 2*w*h + 2*h*l` plus the area of the smallest side.
- **Part 2**: Calculate ribbon length: smallest perimeter `2*(l+w+h - max(l,w,h))` plus volume `l*w*h`.

## Day 03: Perfectly Spherical Houses in a Vacuum
- **Part 1**: Track visited coordinates in a set. Move Santa based on `^v<>`.
- **Part 2**: Use two positions (Santa and Robo-Santa). Alternate moves between them and track all visited coordinates in a shared set.

## Day 04: The Ideal Stocking Stuffer
- **Part 1**: Brute-force MD5 hashes of `secret + number` starting from 0 until a hash starts with `00000`.
- **Part 2**: Continue searching until a hash starts with `000000`.

## Day 05: Doesn't He Have Intern-Elves For This?
- **Part 1**: Check for 3 vowels, double letter, and no forbidden substrings (`ab`, `cd`, `pq`, `xy`).
- **Part 2**: Check for pair appearing twice (non-overlapping) and repeat letter with one between (`xyx`).

## Day 06: Probably a Fire Hazard
- **Part 1**: Simulate a 1000x1000 boolean grid. Process `turn on`, `turn off`, `toggle` instructions.
- **Part 2**: Use an integer grid for brightness. `turn on` (+1), `turn off` (-1, min 0), `toggle` (+2).

## Day 07: Some Assembly Required
- **Part 1**: Recursive evaluation with memoization to resolve wire signals based on gates (AND, OR, LSHIFT, RSHIFT, NOT).
- **Part 2**: Override wire `b` with Part 1's signal for wire `a`, reset cache, and re-evaluate `a`.

## Day 08: Matchsticks
- **Part 1**: Calculate code length vs memory length using `eval()` or manual escape parsing.
- **Part 2**: Calculate encoded length vs code length. Escape backslashes and quotes.

## Day 09: All in a Single Night
- **Part 1**: TSP. Parse distances, generate permutations of cities, find minimum path length.
- **Part 2**: Find maximum path length from the same permutations.

## Day 10: Elves Look, Elves Say
- **Part 1 & 2**: Implement "Look-and-Say" sequence generation. Iterate 40 and 50 times respectively. Used `itertools.groupby`.

## Day 11: Corporate Policy
- **Part 1**: Increment string like base-26 number. Validate rules (straight of 3, no i/o/l, two pairs).
- **Part 2**: Find next valid password after Part 1 result.

## Day 12: JSAbacusFramework.io
- **Part 1**: Regex extraction of all numbers in the JSON string and sum them.
- **Part 2**: Parse JSON. Recursively sum numbers, but ignore objects (dicts) containing the value "red".

## Day 13: Knights of the Dinner Table
- **Part 1**: TSP variation. Maximize total happiness for circular seating.
- **Part 2**: Add "Me" with 0 happiness change to everyone. Re-calculate max happiness.

## Day 14: Reindeer Olympics
- **Part 1**: Calculate distance traveled by each reindeer after 2503 seconds using cycle time (fly + rest).
- **Part 2**: Simulate second-by-second. Award points to leaders at each second.

## Day 15: Science for Hungry People
- **Part 1**: Find ingredient mix (sum 100) maximizing score (product of properties). Used recursion/partitions.
- **Part 2**: Filter combinations to only those with 500 calories.

## Day 16: Aunt Sue
- **Part 1**: Filter Sues based on exact property matches.
- **Part 2**: Filter with ranges for cats/trees (> target) and pomeranians/goldfish (< target).

## Day 17: No Such Thing as Too Much
- **Part 1**: Find all combinations of containers summing to 150L.
- **Part 2**: Find combinations using the minimum number of containers.

## Day 18: Like a GIF For Your Yard
- **Part 1**: Game of Life simulation on 100x100 grid for 100 steps.
- **Part 2**: Same simulation, but the four corner lights are always stuck on.

## Day 19: Medicine for Rudolph
- **Part 1**: Generate all distinct molecules one step away using replacements.
- **Part 2**: Greedy reverse search (reduce molecule to 'e') to find minimum steps.

## Day 20: Infinite Elves and Infinite Houses
- **Part 1**: Sum of divisors * 10. Find first house >= input. Used array sieve.
- **Part 2**: Sum of divisors * 11, but each elf visits only 50 houses.

## Day 21: RPG Simulator 20XX
- **Part 1**: Simulate battles. Iterate all item loadouts (weapon + armor + rings). Find min cost to win.
- **Part 2**: Find max cost to lose.

## Day 22: Wizard Simulator 20XX
- **Part 1**: BFS/Dijkstra on game state (hp, mana, boss_hp, effects). Find min mana to win.
- **Part 2**: Hard mode (player loses 1 HP per turn). Same search.

## Day 23: Opening the Turing Lock
- **Part 1**: Simulate assembly instructions (`hlf`, `tpl`, `inc`, `jmp`, `jie`, `jio`). Start `a=0`.
- **Part 2**: Run simulation with `a=1`.

## Day 24: It Hangs in the Balance
- **Part 1**: Partition weights into 3 groups of equal weight. Minimize count then QE of first group.
- **Part 2**: Partition into 4 groups.

## Day 25: Let It Snow
- **Part 1**: Calculate index in diagonal grid. Compute code using modular exponentiation `start * mul^(index-1) % mod`.
- **Part 2**: Free star!
