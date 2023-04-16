<!-- PROJECT INFO -->
<br />
<div align="center">
  <h1 align="center">ilscrape</h1>
  <p align="center">
    A python mini script to scrap image links from multiple URLs based on search tags!
  </p>
</div>

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may set up this project locally.
To get a local copy up and running please follow these simple steps.

### Prerequisites

---

- Download the repository manually or use `git clone`:

  ```sh
  git clone https://github.com/inaaki/ilscrape.git
  cd ilscrape
  ```

- Install required dependency: ( virtual environment is recommended )

  Unix/MacOS

  ```sh
  python3 -m pip install -r requirements.txt
  ```

  Windows

  ```sh
  py -m pip install -r requirements.txt
  ```

### Usage

---

Open the terminal in the **project directory** and run:

```sh
python3/py main.py "Multiple URLs separated by space" "search tags separated by space"
```

Example:

- Unix/MacOS

  ```sh
  python3 main.py "https://unsplash.com https://picsum.photos" "sky table computer 354"
  ```

- Windows

  ```sh
  py main.py "https://unsplash.com/ https://picsum.photos/" "sky table computer 354"
  ```
