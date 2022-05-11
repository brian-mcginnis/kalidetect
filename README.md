# kali_stats.py

kali_stats is a python program that takes an architecture argument and searches the relevant kali-dev repository ([link](https://http.kali.org/kali/dists/kali-dev/main/)) for the Top 10 packages by number of files. 

It accomplishes this by first scraping the website for supported architecture types then checking against the argument for validity. It then will download the file if it does not exist in the launch directory. Finally it will parse the .gz repository for the packages with the most files and output it to the console.

## Features
* Object Oriented Modularity
* Multi architecture arguments
* Smart argument checking web-scraping

## Ex. Usage Case
The following usage case downloads the .gz kali-dev repository files for the arm64 architecture.

```bash
> python3 kali_stats.py arm64
```
```python
Found File ( 1 of 1 ) 'Contents-arm64.gz' in Directory
Running Analysis on architecture 'arm64'
Reading package files

File Results ( 1 of 1 )

           #                      Package                                # Files
           ---------------------------------------------------------------------------
           1. x11/papirus-icon-theme                                       111368
           ---------------------------------------------------------------------------
           2. fonts/fonts-cns11643-pixmaps                                 110999
           ---------------------------------------------------------------------------
           3. math/sagemath-doc                                             90708
           ---------------------------------------------------------------------------
           4. fonts/texlive-fonts-extra                                     86800
           ---------------------------------------------------------------------------
           5. doc/vtk9-doc                                                  65623
           ---------------------------------------------------------------------------
           6. doc/trilinos-doc                                              62558
           ---------------------------------------------------------------------------
           7. science/ortools-examples                                      59458
           ---------------------------------------------------------------------------
           8. devel/piglit                                                  53007
           ---------------------------------------------------------------------------
           9. x11/obsidian-icon-theme                                       48829
           ---------------------------------------------------------------------------
          10. utils/exploitdb                                               46015
           ---------------------------------------------------------------------------
Program complete
Exiting...
```

## Future plans
* add arguments for setting Top 'n' number of Packages to display
* custom url to support multiple debian based repositories
* add load bar and time
* try/except error reporting

## License
[MIT](https://choosealicense.com/licenses/mit/)
