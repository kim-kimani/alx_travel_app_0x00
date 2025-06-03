# 🏡 ALX Travel App - Project README

> A Django-based travel accommodation listing and booking system.

This project is part of the ALX Software Engineering curriculum. It demonstrates core backend development concepts including database modeling, API serializers, and custom management commands.

---

## 📁 Project Overview

The application allows users to:

- View property listings
- Make bookings
- Leave reviews

It includes:
- Custom Django models (`Listing`, `Booking`, `Review`)
- REST API serializers using Django REST Framework
- A custom command to seed the database with sample data

---

## 🧱 Models

### Listing
- `title`: Name of the property
- `description`: Brief description
- `location`: City or area
- `price_per_night`: Cost per night
- `created_at`: Auto-generated timestamp

### Booking
- `listing`: Foreign key to Listing
- `user_name`: Name of the person booking
- `start_date`: Check-in date
- `end_date`: Check-out date
- `total_price`: Calculated total cost
- `created_at`: Auto-generated timestamp

### Review
- `listing`: Foreign key to Listing
- `user_name`: Name of the reviewer
- `rating`: 1–5 stars
- `comment`: User feedback
- `created_at`: Auto-generated timestamp

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/alx_travel_app_0x00.git 
cd alx_travel_app_0x00