# K-MEANS CONVERTER ASCII ART

> ⚠️ This is clearly not the most efficient way to do an ascii art converter. The program exists to show a funny usecase of the K-Means algorithm.


## Command line

> ⚠️ Don't forget to install modules listed inside `requirements.txt`

```
python main.py picture -c COMPRESSION -g NB_GROUP -o OUTPUT
```

| Param | Description | Optional |
|-------|--------------|--------------|
| `picture` | Path to the picture to convert | No |
| `-g`, `--nb_group` | Number of cluster you want for your K-Means algoritm, default 20 | Yes |
| `-c`, `--compression` | Percentage of compression, default 0% | Yes |
| `-o`, `--output` | File to store the result by default the result will be print in the terminal | Yes |


## Workflow

<p align="center">
  <img src="https://github.com/TheBaronMc/K-Means-converter-ASCII-art/blob/master/worklfow.png?raw=true" />
</p>

## Inspiration

+ [K-means & Image Segmentation - Computerphile](https://www.youtube.com/watch?v=yR7k19YBqiw)
+ [Resizing Images - Computerphile](https://www.youtube.com/watch?v=AqscP7rc8_M)
