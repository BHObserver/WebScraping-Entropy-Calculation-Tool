# WebScraping - Entropy Calculation Tool

This tool automates the process of uploading DNA or protein sequence files to a website that calculates Shannon entropy using phylogenetics. It utilizes web scraping techniques with Selenium to interact with the website's interface, submit files, and download the entropy results.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgment](#acknowledgment)

## Overview

The tool is designed to streamline the process of calculating Shannon entropy for DNA or protein sequence alignments. It performs web scraping to interact with the website, automating the submission of sequence files and downloading of entropy results.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/WebScraping-Entropy-Calculation-Tool.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download and install ChromeDriver from [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/) and make sure it's in your system's PATH.

## Usage

1. Place your DNA or protein sequence files in the specified folder.

2. Run the script:

    ```bash
    python entropy_tool.py
    ```

3. The script will process each file, perform web scraping to upload it to the website, and rename the downloaded entropy results.

## Dependencies

- [Selenium](https://pypi.org/project/selenium/): Python library for automating web browsers.

## Contributing

If you would like to contribute to the project, feel free to open an issue or submit a pull request. Your contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Author

👤 **Burhan Uddin**

- GitHub: [Burhan Uddin](https://github.com/BHObserver/)
- Twitter: [Burhan Uddin](https://twitter.com/BurhanU14173360)
- LinkedIn: [Burhan Uddin](https://www.linkedin.com/in/bhobserver/)

## Acknowledgment

Special thanks to [https://www.hiv.lanl.gov/content/index](https://www.hiv.lanl.gov/content/index) for providing the platform used by this tool.
