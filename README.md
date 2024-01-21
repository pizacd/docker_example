# docker_example

The script is simple, but it's worthwhile to practice execuiting Python scripts using containerization.

After cloning the repository, run the following line in the same directory:
`docker build -t my-welcome-app .`

Once the Docker image is created,  run the following command:
`docker run my-welcome-app`

You should receive a message from your favority version control repository!
