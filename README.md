# 🐶 DevOps Dog Monitoring API

## 📌 Project Overview
This project is a Flask-based REST API designed for dog monitoring and status checking. It is built as part of the DevOps Midterm Assignment to demonstrate modern DevOps practices, including multi-branch version control, automated CI/CD pipelines, automated testing, cloud deployment, and basic health monitoring.

- **Framework:** Python Flask
- **Deployment Platform:** Vercel
- **CI/CD Tool:** GitHub Actions

---

## ⚙️ CI/CD Pipeline Architecture
The project utilizes a 3-stage automated GitHub Actions workflow defined in `.github/workflows/ci-cd.yml`:

1. **Build Stage:** Sets up the Python environment, installs dependencies, and prepares the workspace.
2. **Test Stage:** Runs automated unit tests (`unittest`) on the application to ensure code quality and endpoint stability.
3. **Deploy Stage:** Automatically triggers deployment logic upon successful build and test execution.

---

## 🩺 Monitoring & Health Check
A custom Python script (`monitor.py`) checks the health status of the application endpoint and logs the responses to `health_check.log`.

Run the monitor locally:
```bash
python monitor.py