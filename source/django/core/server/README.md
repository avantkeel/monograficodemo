## ⚠️ Deprecated: `server` Application

The `server` application is **deprecated** and is no longer actively maintained.

### 📌 Background

This app was originally designed to act as a backend layer for a React frontend, exposing API endpoints and handling server-side logic for a decoupled architecture.

However, the project direction has since shifted to a **full-stack Django approach**, where both frontend and backend are handled within Django itself.

### 🚫 Current Status

* No longer in active development
* May contain outdated or unused code
* Not aligned with the current architecture
* Not guaranteed to work with the rest of the project

### ⚠️ Recommendation

* Avoid using the `server` app for new features
* Do not rely on it for production use
* Consider removing it if it becomes unnecessary

### 🔮 Future Consideration

The `server` app may serve as a **reference or starting point** if the project transitions back to a decoupled architecture (e.g., migrating the frontend to React in the future).

### ✅ Current Approach

All backend and frontend functionality should be implemented within the maintained Django apps (e.g., `applications/*`) following the current full-stack design.

---

If you want, I can tighten this into a **more “enterprise-style” README** (shorter, stricter tone) or make it sound more like a **personal project narrative**.
