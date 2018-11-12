# Solr on Ubuntu-18.04.1

## Setup (https://www.howtoforge.com/tutorial/how-to-install-and-configure-solr-on-ubuntu-1604/)
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
    http://yourip:8983/solr
    ```

## Index creation

### Desired output:
<add>
<doc>
<field name="message_id">18104010.1075855725437.JavaMail.evans@thyme</field>
<field name="date">Mon, 26 Mar 2001 09:05:00 -0800 (PST)</field>
<field name="from">mary.gray@enron.com</field>
<field name="to"></field>
<field name="subject">Re: NGI access to eol</field>
<field name="from_name">Phillip K Allen</field>
<field name="to_name">Mary Griff Gray</field>
<field name="content">Grif,

Please provide a temporary id

Phillip
---------------------- Forwarded by Phillip K Allen/HOU/ECT on 03/26/2001 
05:04 PM ---------------------------


Dexter Steis <dexter@intelligencepress.com> on 03/26/2001 02:22:41 PM
To: Phillip.K.Allen@enron.com
cc:  
Subject: Re: NGI access to eol


Hi Phillip,

It's that time of month again, if you could be so kind.

Thanks,

Dexter

*****************************
Dexter Steis
Executive Publisher
Intelligence Press, Inc.
22648 Glenn Drive Suite 305
Sterling, VA 20164
tel: (703) 318-8848
fax: (703) 318-0597
http://intelligencepress.com
http://www.gasmart.com
******************************


At 09:57 AM 1/26/01 -0600, you wrote:

>Dexter,
>
>You should receive a guest id shortly.
>
>Phillip
</field>
</doc>
</add>