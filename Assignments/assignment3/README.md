### Assignment 3

#####Part 1: Driving Directions

  0. Easy mode: `./routing/runroute.sh`
  1. `cd routing`
  2. `python route.py Indianapolis,_Indiana Chicago,_Illinois bfs`

This problem ended up being more hands-on than I expected. The outline of my solution goes like this: read the road segments from road-segments.txt into a list (useful for referencing later), create a version of the list as a dictionary with keys as cities and their respective values as the cities that a road goes to (nodes and edges), run the user's preferred algorithm on the dictionary form, then print the results while referencing back to the information from the list.

I had quite a few problems implementing dfs and bfs at first. It didn't occur to me until I had a working implementation that python is not optimized for tail recursion; when I finally got around to running examples on the full dataset I ran into a stackoverflow within a few seconds. There was an [extremely helpful tutorial for the two algorithms](http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/) that ended up inspiring my final solutions quite a bit.

Depth-first-search and breadth-first-search are both inefficient under different circumstances.

Depth-first-search is usually thought to be the more efficient of the two (at least in practic), but in this situation it went two ways: it found the solution in less than a second, or it ran for close to ten minutes. I think this happens because of the order that the stack is evaluated in, first-in-first-out potentially leaves your solution at the very bottom. Especially when the cities were geographically close together it seemed like dfs would be looking on the wrong side of the country.

Breadth-first-search is slow unless the cities are next to each other. The route it produces is usually much more efficient than the sprawling mess that DFS might create (in one case I watched DFS route completely around the target state), in terms of mileage it would usually be about half the driving distance of the alternative.

I'll be sure to use DFS if I'm ever on a road trip, it seems like the navigational equivalent of Google's "I'm feeling Lucky" button in terms of route distance. BFS is better, though slower, and has the additional benefit of producing short lists (good if you don't want to change roads often), I'll use this if the destination is what I'm interested in.

#####Part 2: Web Scraping

  0. Easy mode: `./crawling/runcrawl.sh`
  1. `cd crawling`
  2. `python crawl.py https://en.wikipedia.org/wiki/Web_scraping 200 pages/ bfs`

I wasn't too enamored with scrapy, so I took a shot at writing my own scraper since I'd used BeautifulSoup before.

I'd mostly used it to extract text, and was aware that BeautifulSoup wasn't perfect; but extracting links and following them with confidence took a lot more considerations than I expected. I figured there were about four situations I was interested in: '/', '//', 'http://', and 'https://'. Filling in the missing blanks wasn't always clear though:

  * are '//' a relative link to the same site or does http belong in front of it? 
  * should '/' simply be corrected by dropping the url in front of it?

On top of that, there were other errors that I had to build in exception protection from: URLError in urllib2 and a UnicodeEncodeError showed up in a few cases. .pdf files caused some issues.

There was also one interesting error that I only encountered once: the script got [stuck inside of Facebook on a page warning the user that it was leaving Facebook](https://www.facebook.com/l.php?u=http%3A%2F%2Fmomentsapp.com%2F&h=HAQFLyA38&s=1), but every time it followed a link Facebook generated a new page with php, creating an infinite loop that depth-first search kept trying to dig deeper into. When I investigated the site it seemed to be some kind of advertisement for an app.

It's probably worth mentioning that my crawler did not take robots.txt into account, to compensate I only ran the script on my local machine through my home WiFi. The speed at which it was even possible to make requests was a bottleneck that kept it well below one page per second though.