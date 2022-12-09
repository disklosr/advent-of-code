### Day 08

Part1: I realized halfway through the first part that I'd better use numpy as slicing rows and columns is faster and less error-prone. My venv did not contain pip so I couldn't install numpy and wasted 10mn trying to fix the issue before I gave up, knowing that without numpy there'll be more debugging to be done

Part2: As expected more debugging was needed for part 2. I had the correct logic but the results weren't correct. It was sadly due to a nasty off by one error that costed me at least 20m

### Day 09

This is one of those puzzles that seem complex at first glance, you then spend precious time trying to figure out how to approach the monster, only to find out later that the solution is rather simple.

The problem tries to simulate movements of a rope as it moves. It starts up with a simple case of a rope of only two points, head and tail, then generalizes it for a rope of N points. In other words, it's a snake game where there are no obstacles, ie the snale has an infinite world and it can go through itself without dying. How cool is that!

Part1: As the problem seemed complex at first, I was thinking about how to represent an infinite world where the snake would move. I had no idea about how to approach that so I did a first simulation to estimate my input's range so I can build a world that can fit thos limits. But by doing that, I realized that it's not needed, I only had to keep track of coordinates of two points moving them according to the input. Took me about half an hour to figure that out.

Part2: It was a piece of cake. It's a generalization of part 1 and was pretty straight forward. However I wasted time with a stupid bug where I was updating the result inside of a loop instead of outside it because I forget to move the instruction outside of it. Reading the requirements again helped me realize the issue. After I moved the problematic line of code to the right place, the result was correct


I solved the two parts in 1h:45mn, remove a 45mn of stupid bugs and fighting with the language and libraries, and it'll be a 1h of pure problem solving. The top competitive programmers did it in less than 8 minutes. Which I find reasonable because with enough experience one should figure out rapidly it's about implementing a simple snake game.

Today's problem is my favorite so far. Although I misjudge it at first as being a complex problem, which is clearly a lack of experience on my part, I find the solution surprizingly simple and the visualizations for debugging pretty cool. Fun times.