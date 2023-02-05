## What is FormData?

The FormData interface provides a way to construct **a set of key/value pairs**(think of a document with lots of field to fill in) representing form fields and their value

## Fast API
- The way HTML forms (<form></form>) sends the data to the server normally uses a "special" encoding for that data, it's different from JSON.
- Data from forms is normally encoded using the "media type" ```application/x-www-form-urlencoded```.
- But when the form includes files, it is encoded as ```multipart/form-data```.

## References
- https://fastapi.tiangolo.com/tutorial/request-forms/#import-form
- https://www.educative.io/answers/what-is-a-formdata-object-in-javascript
- https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data