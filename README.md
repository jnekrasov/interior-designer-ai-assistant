# Interior Designer AI Assistant

This project is an AI-powered assistant that helps users generate interior design ideas based on specific inputs. It uses machine learning models to process images and text inputs to suggest design layouts, color schemes, and furniture arrangements tailored to the user's preferences.
Interior Designer AI Assistant Prototype's implementation using Autogen colloborative agents approach, GPT-4V, Stable diffusion and ComfyUI.

## Features

- **Image Processing**: Analyze images of rooms or furniture to generate design suggestions.
- **Text-based Recommendations**: Input descriptions of your ideal room, and the assistant will suggest a design layout, furniture, and decor.
- **Customization**: Allows users to provide specific preferences such as color schemes, room size, and style (modern, rustic, minimalist, etc.).
- **3D Room Visualization**: Create a virtual model of the room with suggested furniture and decor to help users visualize their design ideas.
- **Integration with Furniture Stores**: Provides links to purchase recommended furniture items from popular retailers.

## Table of Contents

1. [Technologies](#technologies)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Endpoints](#endpoints)
5. [Example Request and Response](#example-request-and-response)
6. [Error Handling](#error-handling)
7. [Contributing](#contributing)
8. [License](#license)

## Technologies

- **Flask**: Backend API framework to handle requests and responses.
- **Python**: Programming language used to build the core application.
- **OpenAI GPT-3**: AI model for generating design suggestions and descriptions.
- **TensorFlow**: Machine learning library used for image processing and analysis.
- **3D Rendering**: Tools to create virtual 3D models of rooms and furniture layouts.

## Installation

### Prerequisites

- Python 3.8+
- Pip (Python package installer)
- Virtual environment (optional, but recommended)

### Steps

1. Clone the repository:

    ```
    git clone https://github.com/jnekrasov/interior-designer-ai-assistant.git
    ```

2. Navigate to the project directory:

    ```
    cd interior-designer-ai-assistant
    ```

3. (Optional) Create and activate a virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

4. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Run the application:

    ```
    python app.py
    ```

    By default, the app will run on `http://127.0.0.1:5000`.

## Usage

### Running the Application

Once the app is running, you can interact with the AI assistant via HTTP requests. Use tools like Postman or cURL to send requests, or integrate it into your own frontend interface.

### Sending a Request

You can send either text-based descriptions or image data to the assistant. The assistant will return recommendations in JSON format, including a breakdown of the suggested design elements.

### Example Input

#### Text Input Example:
```
{
    "room_description": "A small modern living room with large windows, a grey couch, and a wooden coffee table. The walls should be light blue."
}
```

#### Image Input Example:
Send an image in a multipart/form-data request where the `image` key holds the image file.

## Endpoints

### `POST /design-suggestion`

This endpoint accepts either a room description in text format or an image of the room. It returns suggestions for room layout, furniture, color schemes, and decor.

- **URL**: `/design-suggestion`
- **Method**: `POST`
- **Request Format**: 
  - Text input (`application/json`)
  - Image input (`multipart/form-data`)

### Parameters:

- **`room_description`** (optional, string): A text description of the room you want to design.
- **`image`** (optional, file): An image file of the room.

### Response:

```
{
  "layout": "modern",
  "color_scheme": "light blue and grey",
  "furniture_suggestions": [
    {
      "item": "Grey Couch",
      "link": "https://example.com/product/grey-couch"
    },
    {
      "item": "Wooden Coffee Table",
      "link": "https://example.com/product/wooden-coffee-table"
    }
  ],
  "decor_suggestions": [
    "Large framed abstract art",
    "Potted plants"
  ],
  "3d_model_link": "https://example.com/3d-model-link"
}
```

### `GET /health-check`

This endpoint checks if the API is running properly.

- **URL**: `/health-check`
- **Method**: `GET`
- **Response**: 
```
{
  "status": "running"
}
```

## Example Request and Response

### Text-Based Request:

**Request:**

```
curl -X POST http://127.0.0.1:5000/design-suggestion \
  -H "Content-Type: application/json" \
  -d '{
    "room_description": "A small modern living room with a grey couch and wooden coffee table."
  }'
```

**Response:**

```
{
  "layout": "modern",
  "color_scheme": "light grey and natural wood",
  "furniture_suggestions": [
    {
      "item": "Grey Sofa",
      "link": "https://furniturestore.com/product/grey-sofa"
    },
    {
      "item": "Wooden Coffee Table",
      "link": "https://furniturestore.com/product/wood-coffee-table"
    }
  ],
  "decor_suggestions": [
    "Minimalist framed art",
    "A potted plant in the corner"
  ]
}
```

### Image-Based Request:

You can use Postman or any other API client to upload an image for room analysis and suggestions. 

## Error Handling

If there is an error in the request (e.g., missing data), the API will return an error response with a relevant message.

**Example Error Response:**

```
{
  "error": "Invalid request",
  "message": "Please provide a room description or an image."
}
```

## Contributing

We welcome contributions! If you have suggestions or improvements:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

### Running Tests

To run the tests, you can use:

```
pytest tests/
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
You can watch the development process and follow along on YouTube here: [Watch the video](https://www.youtube.com/watch?v=lmH4wJJIGZk).
