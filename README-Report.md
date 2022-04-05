3 components:

- GitHub Actions -> a remote virtual environment where my code is tested with pytest and if the tests succeed the digitalocean server is updated with it

- DigitalOcean -> a remote server where I run a virtual linux server on NGINX and Gunicorn

- Bash -> this is a Linux shell which a used to communicate with my server


At first I did not completely understand the assignment, I struggled a while but couldn't
get over the idea that nothing was said about the code we had to write and check with
Github Actions. I reached out to Rishaan, he helped me understand that this assignment
was not about the python code, Hello World was enough to see in the browser.

Following the instructions for gunicorn of the Deployment exercise I got an error message, I could not start the app. Looked like it did not recognize me as a user. I doublechecked everything for typo’s or other stupid mistakes and when nothing found I asked on Slack, Rishaan checked per videocall and could not find a mistake. I had seen that Lucas also had a problem at this point, although it was another error I suggested trying his solution. We did and it helped! It looks like there is an error in the farm.service example in the Deployment exercise. To be exactly in ExecStart=/usr/local/bin/gunicorn main:app  When I adjust this to ExecStart=gunicorn main:app it works! I also came across this problem in the CD assignment.  

The biggest problem I encountered was that I could ssh to my server but it was not possible to go to the directory which I wanted to update (using cd /home/cd/) with a git pull request. I struggled a whole weekend with this. As on Monday there still was nobody who could help me understand what I was doing wrong I started over, using a new repository and another action from the Marketplace, now I had it all working within a few hours! 


