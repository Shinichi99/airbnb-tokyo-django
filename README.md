# Airbnb Pricing Optimization App

![Project Image](./airbnb_tokyo_app/static/img/img1.png)

The [**Airbnb Pricing Optimization App**](https://airbnb-tokyo-django.onrender.com) is a tool designed to help hosts in Tokyo optimize the pricing of their accommodation facilities on Airbnb. It uses a machine learning model built on XGBoost to predict the optimal price for accommodations, taking into account various features and attributes of the listing. The model is based on the latest data from September 2023 and has a coefficient of determination (R-squared) of 0.7, indicating a high level of prediction accuracy.

## Table of Contents
- [Overview](#overview)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Feature Engineering](#feature-engineering)
- [Model Building](#model-building)
- [Web Deployment](#web-deployment)
- [Getting Started](#getting-started)
- [Data Source](#data-source)) 

## Overview

The prices of accommodation facilities on Airbnb can vary significantly based on factors such as location, room type, amenities, and more. This app helps hosts determine the most suitable price for their listings by considering a wide range of attributes. Key project highlights include:

- Utilizing machine learning to make accurate price predictions.
- Incorporating data from approximately 10,000 accommodation facilities in Tokyo.
- Addressing the challenge of price variability in Airbnb data.

## Exploratory Data Analysis

One of the challenges in price prediction for Airbnb listings is the wide range of prices set by individual hosts. Despite this variability, the model aims to use the relationships between price and other attributes to make accurate predictions.

## Feature Engineering

One crucial feature used in the model is "Transport Accessibility." It considers the distance from the nearest station as well as the distances to major railway stations in Tokyo. These factors play a significant role in determining the price of an accommodation.

## Model Building

The machine learning model is built on the XGBoost framework and is trained on data from around 10,000 accommodation facilities in Tokyo. The model achieves a coefficient of determination of 0.7, indicating a high level of prediction accuracy. However, it's important to note that high-priced accommodation facilities may have some prediction challenges.

## Web Deployment

The app is deployed on the Render platform and is developed using Django, which facilitates rapid development and provides a clean, pragmatic design. Bootstrap is utilized for an attractive and user-friendly app design.

## Getting Started

To use the Airbnb Pricing Optimization App, visit the [web application](https://airbnb-tokyo-django.onrender.com) and enter the details of your accommodation listing. The app will provide you with a predicted optimal price based on the information you provide.

## Data Source

- Airbinb data for Tokyo was obtained from [Inside Airbnb](http://insideairbnb.com/get-the-data.html).
- Train station data was obtained from [駅データ．ｊｐ](https://ekidata.jp/dl/).



