from diagrams import Diagram
from diagrams.aws.storage import S3
from diagrams.k8s.compute import Pod
from diagrams.onprem.queue import Kafka

with Diagram("Kafka Connect", filename="consumer", show=False):
    Pod("consumer") >> Kafka("broker") >> S3("event-sink")
