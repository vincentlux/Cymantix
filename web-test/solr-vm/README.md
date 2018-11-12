# Solr on Ubuntu-18.04.1

## Setup
* Log into Ubuntu-18.04.1 vm
* Install JVM
    ```
    sudo apt-get software-properties-common
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get install oracle-java8-installer
    ```
* Install Solr 
    ```
    cd /tmp
    wget http://www.us.apache.org/dist/lucene/solr/7.5.0/solr-7.5.0.tgz
    tar xzf solr-7.5.0.tgz solr-7.5.0/bin/install_solr_service.sh --strip-components=2
    sudo ./install_solr_service.sh solr-7.5.0.tgz
    ```
* Creating a Solr search collection
    ```
    sudo su - solr -c "/opt/solr/bin/solr create -c gettingstarted -n data_driven_schema_configs"
    ```
* Open port
    * Firewall open port 8983
    * ufw open port
    ```
    sudo ufw allow 8983/tcp
    ```
* Use web interface
    ```
    http://104.248.61.45:8983/solr
    ```