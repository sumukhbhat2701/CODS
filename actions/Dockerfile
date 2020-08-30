FROM rasa/rasa-sdk:latest

 # The Rasa SDK image runs as non-root user by default. Hence, you have to switch
 # back to the `root` user if you want to install additional dependencies'
COPY ./actions /app/actions
USER root

RUN pip3 install actions && pip3 install google && pip3 install typing==3.7.4.3 && pip3 install tweepy==3.8.0 && pip3 install beautifulsoup4==4.9.0 && pip3 install numpy==1.17.1 && pip3 install pandas==1.0.3 && pip3 install matplotlib==3.2.2 && pip3 install scipy==1.4.1 && pip3 install rasa==1.10.2 && pip3 install nltk==3.4.5 && pip3 install tensorflow==2.1.0 

# Switch back to a non-root user
USER 1001

VOLUME ["/app/actions"]

EXPOSE 5055

CMD ["start", "--actions", "actions.actions"]
