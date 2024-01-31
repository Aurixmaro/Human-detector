# Human-detector

The project aimed to create an API that has 3 GET endpoints that read a photo from the disk and return information about how many people were found in the photo. The second GET which in the parameter receives a link to a photo that is on the Internet, downloads it and then returns information about how many people were found in the photo. The third POST is where you can upload a photo and then returns information about how many people were found in the photo.

The applications were concentrated using Docker, and the application image was placed in the Docker registry. CI was also configured for static code analysis under the PEP 8 standard.
