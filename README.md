# Comic Crawler & Downloader

A powerful OOMOL workflow package that automatically downloads comic images from web pages and converts them into digital comic books.

## What Does This Package Do?

This package helps you turn any comic webpage into a downloadable digital comic book. Simply provide a comic webpage URL, and the package will:

1. **Extract comic images** from the webpage
2. **Download all images** automatically
3. **Create a digital comic book** in your preferred format (EPUB, CBZ, or PDF)

## Who Is This For?

- **Comic enthusiasts** who want to read comics offline
- **Digital library builders** who collect comics
- **Anyone** who wants to preserve web-based comics locally

## Main Features

### 🌐 Web Comic Extraction
- Analyzes any comic webpage and intelligently identifies comic images
- Handles various comic website formats automatically
- Sorts pages in correct reading order

### 📥 Automatic Download
- Downloads all comic images from the webpage
- Organizes files properly for comic book creation
- Handles different image formats and sizes

### 📚 Digital Book Creation
- Converts downloaded images into digital comic formats:
  - **EPUB**: For e-readers like Kindle, Kobo
  - **CBZ**: Standard comic book archive format
  - **PDF**: Universal format for any device

### 🎨 Smart Processing
- Automatically generates appropriate file names
- Maintains proper page order for reading
- Filters and processes only image files

## How It Works

### Simple 3-Step Process

1. **Input**: Provide the URL of a comic webpage
2. **Processing**: The workflow automatically:
   - Crawls the webpage content
   - Identifies comic images using AI
   - Downloads all images in order
   - Creates the digital comic book
3. **Output**: Get your comic book file ready for reading

### Technical Components

The package includes two main workflow components:

#### Download Image Block
- **Purpose**: Downloads individual comic images
- **Input**: Image URL and save directory
- **Output**: Downloaded image file path
- **Use Case**: Perfect for batch downloading comic images

#### Comic Crawler Workflow
- **Purpose**: Complete comic extraction and book creation
- **Input**: Comic webpage URL and save location
- **Output**: Digital comic book file (EPUB/CBZ/PDF)
- **Features**:
  - AI-powered content analysis
  - Automatic image extraction
  - Book formatting and creation

## Getting Started

### Requirements
- OOMOL platform installed
- Internet connection for downloading
- Storage space for comic files

### Usage
1. Open the Comic Crawler workflow in OOMOL
2. Enter the comic webpage URL
3. Choose your save directory
4. Select output format (EPUB, CBZ, or PDF)
5. Run the workflow
6. Find your digital comic book in the specified directory

## Supported Formats

### Input
- Any webpage containing comic images
- Various comic hosting websites
- Both single-page and multi-page comics

### Output Formats
- **EPUB**: Best for e-readers and mobile devices
- **CBZ**: Standard format for comic book apps
- **PDF**: Universal format for any device

## Example Use Cases

- **Webcomics**: Download ongoing webcomic series
- **Digital Preservation**: Archive comics from websites
- **Offline Reading**: Create local copies for travel
- **Format Conversion**: Convert web comics to readable formats

## Dependencies

This package uses several specialized tools:
- **LLM Integration**: For intelligent content analysis
- **Web Crawler**: For webpage content extraction
- **Image Processing**: For download and organization
- **Archive Tools**: For comic book creation

## Support

This package is designed to work with most comic websites automatically. The AI-powered analysis adapts to different webpage formats and layouts, making it versatile for various comic sources.

---

*Built with OOMOL - Making complex workflows simple and accessible for everyone.*