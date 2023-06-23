# MaxScale Docker image

MaxScale-Docker is a Docker container image that provides a lightweight and portable deployment option for MaxScale, a database proxy for MariaDB and MySQL. It simplifies the process of deploying and managing MaxScale instances in a containerized environment. MaxScale-Docker allows users to easily scale and distribute database traffic while providing advanced features like load balancing, high availability, and routing.


STEP ONE Clone Repo
git clone https://github.com/name/your-project.git



Step 2 Build an image and run the container
docker build -t your-image-name 
docker run -p  your-image-name

Step 3 Make Directory and navigate to that directory
mkdir maxscale-config
mkdir maxscale-config
cd maxscale-config/maxscale

In the maxscale directory you can ls and find the maxscale.cnf 
Open it with sudo nano maxscale.cnf and add configuration

After you've touched up the .cnf you run "Sudo docker-compose up" to see contents
Put -d at the end of command to get a shorter version instead of seeing entire installation

Step 4 Check if servers are up
To check Run sudo docker-compose exec maxscale maxctrl list servers amd ypur output should look similar:


┌─────────┬─────────┬──────┬─────────────┬─────────────────┬──────────┬─────────────────┐
│ Server  │ Address │ Port │ Connections │ State           │ GTID     │ Monitor         │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┼─────────────────┤
│ server1 │ master  │ 3306 │ 0           │ Master, Running │ 0-3000-7 │ MariaDB-Monitor │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┼─────────────────┤
│ server2 │ slave1  │ 3306 │ 0           │ Slave, Running  │ 0-3000-7 │ MariaDB-Monitor │
├─────────┼─────────┼──────┼─────────────┼─────────────────┼──────────┼─────────────────┤                                 
│ server3 │ slave2  │ 3306 │ 0           │ Slave, Running  │ 0-3000-7 │ MariaDB-Monitor │
└─────────┴─────────┴──────┴─────────────┴─────────────────┴─


Docker-compose down to bring down maxscale instance
