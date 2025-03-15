# How to Contribute to the Kanye West Tweet Archive

Thank you for your interest in contributing to the Kanye West Tweet Archive! This guide will walk you through the process of submitting a pull request (PR) and ensuring your contributions are properly organized.

---

## Submission Guidelines

### 1. Tweet Data
- All new tweet data must be submitted in **JSON format**.
- The JSON file should be placed in the `tweets` directory.
- Check the [X Api Docs](https://developer.x.com/en/docs/x-api/v1/data-dictionary/object-model/tweet) for the full json schema:
---

### 2. Media Files
- **Images**: Save images in the highest quality available and retain the original filenames as stored by Twitter. Place them in the `media` directory.
- **Videos**: Save videos in the highest quality available and retain the original filenames as stored by Twitter. Place them in the `videos` directory.
- Ensure the filenames in the JSON file match the actual filenames of the uploaded files.

---

### 3. Profile Images
- Profile images should also be saved in the highest quality available and retain the original filenames as stored by Twitter.
- Place profile images in the `profile_images` directory.
- Ensure the profile image filename in the JSON file match the actual filename of the uploaded file.

---

## How to Submit a Pull Request

### 1. Fork the Repository
- Click the "Fork" button at the top right of the repository page to create your own copy of the archive.

### 2. Clone Your Fork
- Clone your forked repository to your local machine (Note: This repo is around 500MB):
  ```bash
  git clone https://github.com/yetweets/vault.git
  ```

### 3. Create a New Branch
- Create a new branch for your contribution:
  ```bash
  git checkout -b add-tweet-YYYYMMDD
  ```
  Replace `YYYYMMDD` with the date of the tweet you're adding.

### 4. Add Your Files
- Add the tweet JSON file(s) to the `tweets` directory.
- Add media file(s) (images and videos) to the `media` and `videos` directories, respectively.
- Add profile image(s) to the `profile_images` directory.

### 5. Commit Your Changes
- Commit your changes with a descriptive message:
  ```bash
  git commit -m "Add tweet from YYYY-MM-DD with media and profile image"
  ```

### 6. Push Your Changes
- Push your changes to your forked repository:
  ```bash
  git push origin add-tweet-YYYYMMDD
  ```

### 7. Submit a Pull Request
- Go to the original repository on GitHub.
- Click the "New Pull Request" button.
- Select your branch and provide a clear title and description for your PR.
- Submit the PR and wait for it to be reviewed.

---

## Notes
- Ensure all filenames match exactly between the JSON file and the uploaded media/video/profile image files.
- Double-check that media and videos are in the highest quality available.
