I saw this tweet the other day:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Here&#39;s a vey strange Sorting Algorithm:<br><br>For every element X on the sequence the program does this:<br>1) Sleeps for X seconds<br>2) Prints X<br><br>The clock starts simultaneously for all elements.</p>&mdash; Fermat&#39;s Library (@fermatslibrary) <a href="https://twitter.com/fermatslibrary/status/937687947041701888?ref_src=twsrc%5Etfw">December 4, 2017</a></blockquote>

And it seemed like a good opportunity to demonstrate [asyncio](https://docs.python.org/3/library/asyncio.html).

`./sleepsort.py` contains a command line application that can sort positive integers by sleeping. It requires Python 3.7.

If you have [poetry](https://poetry.eustace.io/), you can run:

```
poetry run ./sleepsort.py 6 2 8 3 6 9
```

Run a test (that checks against `sorted`) with

```
poetry run pytest
```
