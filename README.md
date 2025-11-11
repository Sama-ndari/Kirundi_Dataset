<div align="center">

# 🇧🇮 Kirundi Open Speech & Text Dataset

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data License: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/Sama-ndari/Kirundi_Dataset?style=social)](https://github.com/Sama-ndari/Kirundi_Dataset)

*Building the first large-scale, open-source speech and text dataset for Kirundi*

[🚀 Get Started](#-how-to-contribute) • [📊 Dataset](#-dataset-structure) • [🎯 Roadmap](#-project-roadmap) • [🤝 Community](#-community)

</div>

---

## 🌍 About This Project

**Kirundi** is spoken by over 12 million people, yet it remains a **low-resource language** largely ignored by modern AI systems. We're changing that.

This community-driven initiative aims to create the **first comprehensive, open-source speech and text dataset** for Kirundi, enabling the development of:

### 🎯 Target Applications

| Application | Description | Status |
|-------------|-------------|---------|
| 🎙️ **Speech-to-Text (ASR)** | Transcribe spoken Kirundi into text | 🔄 In Progress |
| 🗣️ **Text-to-Speech (TTS)** | Generate natural-sounding Kirundi speech | 📋 Planned |
| 🌐 **Machine Translation** | Translate between Kirundi and other languages | 📋 Planned |
| 🎧 **Speech Translation** | Direct speech-to-speech translation | 📋 Planned |

> **Our Mission**: *Ikirundi c'acu, ijwi ry'acu* - Preserve and digitize our language for future generations.

## 🚀 How to Contribute

<div align="center">

**Every contribution matters! Choose the way that works best for you:**

</div>

### 📝 Option 1: Add Kirundi Text

<details>
<summary><b>🎯 Goal:</b> Collect clean, high-quality Kirundi sentences</summary>

#### 📋 Steps:
1. **Find Sources**: Look for Kirundi text from:
   - 📰 [Kirundi Wikipedia](https://rn.wikipedia.org)
   - 📚 Public domain books
   - 🗞️ News articles
   - 📖 Educational materials

2. **Clean Text**: Remove all non-essential elements:
   - ❌ Dates and numbers
   - ❌ Editorial marks like `[edit]` or `(Akarorero:)`
   - ❌ Non-Kirundi words
   - ✅ Keep only clean, natural sentences

3. **Add to Dataset**:
   ```bash
   # Add sentences to the text file (one per line)
   echo "Your clean Kirundi sentence" >> scripts/kirundi_prompts_scraped.txt
   
   # Run the appender script
   python scripts/append_to_csv.py
   ```

4. **Submit**: Create a Pull Request with your changes

</details>

---

## 🧳 Understanding Git LFS: The "Luggage" System

<div align="center">

**🎯 Why Your Audio Files Go to Hugging Face, Not GitHub**

</div>

### 📦 The Simple Analogy

Think of this project like traveling with luggage:

| Component | Real World | Our Project |
|-----------|------------|-------------|
| 🎒 **Small Backpack** | Your carry-on bag | GitHub/Hugging Face repository |
| 📓 **Notebook** | Small, lightweight item | `metadata.csv` file |
| 🧳 **Heavy Suitcase** | Large, bulky luggage | Audio files (`clips/*.wav`) |
| ✈️ **Luggage Check-in** | Airport baggage service | **Git LFS** (Large File Storage) |

### 🔄 How It Works

1. **Your Repository** (the backpack) holds:
   - ✅ `metadata.csv` - fits perfectly
   - ✅ Code and scripts - small text files
   - ❌ **NOT** the actual audio files (too big!)

2. **Git LFS** (the luggage service) handles:
   - 🎵 All audio files in `clips/` folder
   - 📦 Stores them in Hugging Face's special storage
   - 🏷️ Leaves tiny "luggage tags" (pointers) in your repository

3. **When you push to Hugging Face**:
   - 📝 Normal Git uploads the small files
   - 🚀 Git LFS automatically uploads audio to special storage
   - 🔗 Everything stays connected and accessible

### 🛠️ First-Time Setup (Do This Once)

Before contributing audio, you need to "activate the luggage service":

```bash
# Step 1: Install Git LFS on your computer
# On Ubuntu/Debian:
sudo apt install git-lfs

# On macOS:
brew install git-lfs

# On Windows: Download from https://git-lfs.github.io/

# Step 2: Initialize Git LFS in your repository
git lfs install

# Step 3: Tell Git LFS to handle audio files
git lfs track "clips/*.wav"
git lfs track "clips/*.mp3"

# Step 4: Commit the LFS configuration
git add .gitattributes
git commit -m "Setup Git LFS for audio files"
```

### ✅ What Contributors See

When you contribute audio, your workflow is exactly the same:

```bash
# Normal Git commands work perfectly!
git add clips/your_audio.wav
git add metadata.csv
git commit -m "Added audio recording"
git push
```

**Behind the scenes**: Git LFS automatically handles the heavy lifting, uploading your audio to Hugging Face's storage while keeping your repository fast and lightweight.

> **🎯 Key Point**: Audio files are stored in **Hugging Face's Git LFS storage**, not in the main repository. This keeps everything fast while preserving all your recordings safely.

---

### 🌐 Option 2: Add French Translations

<details>
<summary><b>🎯 Goal:</b> Provide high-quality Kirundi ↔ French translations</summary>

#### 📋 Requirements:
- ✅ Fluent in both Kirundi and French
- ✅ Understanding of cultural context
- ✅ Attention to linguistic nuances

#### 📋 Steps:
1. Open `metadata.csv`
2. Find rows with empty `french_translation` column
3. Add accurate, natural translations
4. Submit a Pull Request

> **💡 Tip**: Focus on preserving meaning and cultural context, not just literal translation.

</details>

---

### 🎤 Option 3: Record Audio (Most Critical!)

<details>
<summary><b>🎯 Goal:</b> Create high-quality Kirundi speech recordings</summary>

#### 🎧 Recording Requirements:
- 🔇 **Quiet environment** (no background noise)
- 🎙️ **Good microphone** (headset or smartphone)
- 📊 **Technical specs**:
  - Format: WAV (preferred) or MP3
  - Sample Rate: 16kHz or 22.05kHz
  - Channels: Mono (1 channel)
  - Bit Depth: 16-bit

#### 📋 Steps:
1. **Setup Git LFS**: Complete the [First-Time Setup](#-first-time-setup-do-this-once) if you haven't already
2. **Fork & Clone**: Fork repository and clone to your computer
3. **Choose**: Open `metadata.csv` and find empty `file_path` entries
4. **Record**: Follow our [Recording Guidelines](#-recording-guidelines)
5. **Save**: Place audio in `clips/` folder (e.g., `rn_0001.wav`)
6. **Update Metadata**:
   ```csv
   file_path,kirundi_transcription,french_translation,speaker_id,age,gender
   clips/rn_0001.wav,"Your sentence",,"speaker_001",20s,female
   ```
7. **Submit**: Create Pull Request with audio + metadata

> **🔒 Privacy**: Use anonymous speaker IDs. Your personal information is never required.

</details>

## 🎧 Recording Guidelines

<div align="center">

**📏 Quality Standards for Audio Recordings**

</div>

### 🎯 Recording Best Practices

| Aspect | Requirement | Why It Matters |
|--------|-------------|----------------|
| 🔇 **Environment** | Quiet room, no background noise | Ensures clean training data |
| 🎙️ **Microphone** | Headset mic or smartphone (close to mouth) | Clear audio capture |
| 🗣️ **Speaking Style** | Natural, clear pronunciation | Realistic speech patterns |
| 📝 **Accuracy** | Read exactly as written | Maintains text-audio alignment |

### ⚙️ Technical Specifications

```yaml
Audio Format:
  - Primary: WAV (uncompressed)
  - Alternative: MP3 (high quality)
  
Settings:
  - Sample Rate: 16kHz or 22.05kHz
  - Channels: Mono (1 channel)
  - Bit Depth: 16-bit
  - Duration: Natural sentence length
```

### 🛠️ Recommended Tools

- **🎵 [Audacity](https://www.audacityteam.org/)** (Free, cross-platform)
- **📱 Smartphone voice recorder** (built-in apps work great)
- **💻 Online recorders** (for quick contributions)

---

## 📊 Dataset Structure

Our dataset is organized around `metadata.csv` - the central hub for all project data.

### 📋 Schema Overview

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `file_path` | String | Relative path to audio file | `clips/rn_0001.wav` |
| `kirundi_transcription` | String | Exact Kirundi sentence | `Amahoro y'Imana abane nawe` |
| `french_translation` | String | High-quality French translation | `Que la paix de Dieu soit avec toi` |
| `speaker_id` | String | Anonymous speaker identifier | `speaker_001` |
| `age` | String | Age group | `20s`, `30s`, `40s+` |
| `gender` | String | Self-identified gender | `male`, `female`, `other` |

### 📁 Directory Structure

```
Kirundi_Dataset/
├── 📄 README.md              # This file
├── 📊 metadata.csv           # Master dataset file
├── 🎵 clips/                 # Audio recordings
│   ├── rn_0001.wav
│   ├── rn_0002.wav
│   └── ...
└── 🔧 scripts/               # Automation tools
    ├── append_to_csv.py      # Add new sentences
    ├── scrapping_kirundi_words.py  # Web scraping
    └── kirundi_prompts_scraped.txt # Raw text input
```

## 🎯 Project Roadmap

<div align="center">

**🚀 Building the Future of Kirundi AI, One Step at a Time**

</div>

### 📈 Development Phases

```mermaid
graph LR
    A[📝 Text Collection] --> B[🌐 Translation]
    B --> C[🎤 Audio Recording]
    C --> D[🤖 Model Training]
    D --> E[🚀 Deployment]
```

| Phase | Goal | Target | Status | Progress |
|-------|------|--------|--------|----------|
| **Phase 1** | 📝 Text Collection | 10,000+ sentences | 🔄 **In Progress** | ![Progress](https://progress-bar.dev/35/) |
| **Phase 2** | 🌐 French Translation | Complete dataset | 📋 Planned | ![Progress](https://progress-bar.dev/0/) |
| **Phase 3** | 🎤 Audio Recording | 20+ hours | 📋 Planned | ![Progress](https://progress-bar.dev/0/) |
| **Phase 4** | 🤖 Model Training | ASR/TTS/MT models | 📋 Planned | ![Progress](https://progress-bar.dev/0/) |
| **Phase 5** | 🚀 Public Release | Open-source models | 🎯 Future | ![Progress](https://progress-bar.dev/0/) |

### 🎯 Current Milestones

- ✅ **Repository Setup**: Project structure and automation scripts
- ✅ **Data Pipeline**: Automated text processing and validation
- 🔄 **Community Building**: Growing contributor base
- 📋 **Quality Standards**: Establishing recording and translation guidelines

---

## 🤝 Community

<div align="center">

**Join our mission to preserve and digitize Kirundi!**

[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289da?style=for-the-badge&logo=discord)](https://discord.gg/your-server)
[![Telegram](https://img.shields.io/badge/Telegram-Join%20Chat-26A5E4?style=for-the-badge&logo=telegram)](https://t.me/your-group)

</div>

### 🌟 Contributors

We thank all our amazing contributors who are helping build this dataset:

<!-- Contributors will be automatically added here -->
<a href="https://github.com/Sama-ndari/Kirundi_Dataset/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Sama-ndari/Kirundi_Dataset" />
</a>

### 📊 Current Stats

| Metric | Count |
|--------|-------|
| 📝 **Total Sentences** | 180+ |
| 🎤 **Audio Recordings** | 0 |
| 🌐 **Translations** | 0 |
| 👥 **Contributors** | Growing! |

---

## ⚖️ License

<div align="center">

| Component | License | Details |
|-----------|---------|---------|
| 🔧 **Code & Scripts** | [![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) | Free to use, modify, and distribute |
| 📊 **Dataset** | [![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) | Open access with attribution |

</div>

### 📜 What This Means

- ✅ **Free to use** for research, commercial, and educational purposes
- ✅ **Attribution required** when using the dataset
- ✅ **No restrictions** on derivative works
- ✅ **Open source** forever

---

<div align="center">

## 💝 Support This Project

**🇧🇮 *Ikirundi c'acu, ijwi ry'acu* 🇧🇮**

*Our language, our voice - Thank you for helping build the future of Kirundi AI*

---

**⭐ Star this repository** • **🔄 Share with friends** • **🤝 Contribute today**

[![GitHub stars](https://img.shields.io/github/stars/Sama-ndari/Kirundi_Dataset?style=social)](https://github.com/Sama-ndari/Kirundi_Dataset)
[![Follow on GitHub](https://img.shields.io/github/followers/Sama-ndari?style=social)](https://github.com/Sama-ndari)

</div>