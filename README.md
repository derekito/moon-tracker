# 🌙 Moon Position Tracker

A web application that tracks the current position of the moon based on geographic location and time. Built with HTML, CSS, and JavaScript, featuring a beautiful 3D visualization of the moon's position in the sky.

## ✨ Features

- **Real-time Moon Tracking**: Calculate moon position for any location and time
- **3D Sky Visualization**: Interactive 3D representation showing moon position relative to horizon
- **Timezone Support**: Automatic timezone detection and location-based coordinates
- **Professional Accuracy**: Uses timeanddate.com API for precise astronomical calculations
- **Responsive Design**: Works on desktop and mobile devices
- **Cardinal Directions**: Clear N, S, E, W markers for orientation

## 🚀 Live Demo

Visit the live application: [Moon Position Tracker](https://yourusername.github.io/moon-tracker/)

## 🛠️ How to Use

1. **Select Timezone**: Choose your timezone from the dropdown
2. **Set Date & Time**: Pick the date and time you want to check
3. **Calculate Position**: Click "Calculate Moon Position"
4. **View Results**: See the moon's azimuth, altitude, and 3D position

## 📊 What You'll See

- **Azimuth**: Direction of the moon (0° = North, 90° = East, etc.)
- **Altitude**: Height above horizon (0° = horizon, 90° = directly overhead)
- **Distance**: Moon's distance from Earth
- **Phase**: Current moon phase
- **3D Visualization**: Interactive sky dome showing moon position

## 🔧 Technical Details

### Technologies Used
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **3D Graphics**: CSS 3D transforms and perspective
- **API**: timeanddate.com Astronomy API
- **Deployment**: GitHub Pages

### Key Features
- **Astronomical Calculations**: Based on professional astronomical algorithms
- **CORS Handling**: Uses proxy for API calls from browser
- **Responsive Design**: Mobile-friendly interface
- **Real-time Updates**: Instant calculation and visualization

## 📁 Project Structure

```
moon-tracker/
├── index.html          # Main HTML file
├── styles.css          # CSS styles and 3D graphics
├── script.js           # JavaScript logic and API calls
├── README.md           # This file
├── .github/workflows/  # GitHub Actions for deployment
└── requirements.txt    # Python dependencies (for local development)
```

## 🌐 API Integration

This application uses the timeanddate.com Astronomy API for accurate moon position calculations. The API provides:

- Precise astronomical data
- Professional-grade calculations
- Real-time position updates
- Reliable and trusted source

## 🚀 Deployment

This project is automatically deployed to GitHub Pages using GitHub Actions. Any push to the main branch triggers a deployment.

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/moon-tracker.git
   cd moon-tracker
   ```

2. Open `index.html` in your browser or serve with a local server:
   ```bash
   python3 -m http.server 8000
   ```

3. Visit `http://localhost:8000`

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you have any questions or issues, please open an issue on GitHub.

---

**Note**: This application requires an internet connection to access the timeanddate.com API for accurate moon position calculations. 