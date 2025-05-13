# SerializerDeserializer


What Happens When You Send This JSON in a POST Request:
{
  "name": "Alice",
  "grade": 10
}
Deserialization (JSON → Python Object)
When you send this JSON in a POST request to your Django API, it is first received as JSON by Django's REST Framework.

The request.data contains this raw JSON data.
The serializer (e.g., StudentSerializer) will convert this JSON into a Python dictionary.
Example:

# request.data after deserialization (Python dictionary)
{
    "name": "Alice",
    "grade": 10
}
Model Conversion (Python Dictionary → Django Model Object)
After the data is deserialized into a Python dictionary, the serializer then takes this data and creates a Python object corresponding to the Django model (Student in your case).

This is done when serializer.save() is called.

For example:

# This is what happens when you call serializer.save()
new_student = Student(name="Alice", grade=10)
new_student.save()  # Saves this object to the database
So, at this point, you now have a Django Student model instance with the name and grade fields populated.
What Happens When You Send a GET Request to Fetch Data:
Once the data has been saved to the database, you can fetch the data with a GET request. The process works like this:

Django queries the database for all the Student objects:
students = Student.objects.all()
The serializer then serializes this list of Python objects (the Student model instances) into JSON.
Example of what happens in the serializer:

# student is a Django model object like:
# student = Student(id=1, name="Alice", grade=10)

# The serializer will convert it into a dictionary like:
{
    "id": 1,
    "name": "Alice",
    "grade": 10
}
This JSON is then returned as the response to the GET request.
Summary of the Full Process:
POST Request:
You send JSON: {"name": "Alice", "grade": 10}.
It is deserialized into a Python dictionary: {"name": "Alice", "grade": 10}.
The serializer then takes that data and creates a Django model object (Student).
The object is saved to the database.
GET Request:
The Django model objects are retrieved from the database.
The serializer converts these model objects into JSON.
The JSON is returned as the response.
Key Points:
POST: You send JSON, and it is converted to a Python dictionary, which is then used to create a Django model object.
GET: The Django model objects are converted back into JSON to send as the response.
