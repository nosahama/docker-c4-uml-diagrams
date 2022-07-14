from diagrams import Diagram, Edge
from diagrams.aws.storage import S3
from diagrams.custom import Custom
from diagrams.k8s.compute import Pod
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka
from icons import RMQ_ICON

with Diagram("Proposed Consumer Retry Flow", filename="consumer_retries", show=False):
    us_pc = Pod("consumer-{provider-type}-{business-unit}")
    rmq_us_p = Custom("tcs-gateway.us \n [us.transactional.salesforce.send]", RMQ_ICON)
    retry_queue = Custom("Retry Queue", RMQ_ICON)

    retry_p = Pod("consumer-{provider-type}-retry")
    retry_metadata_redis = Redis("retry metadata")
    deadletter_queue = Custom(
        "DLQ \n tcs-salesforce-us.dead \n [us.transactional.salesforce.deadletter]",
        RMQ_ICON,
    )

    us_pc >> Edge(
        label="On consumer error, forward event to Retry Queue"
    ) >> retry_queue << retry_p
    retry_p >> Edge(label="Get event retry metadata") >> retry_metadata_redis
    retry_p >> Edge(
        label="Move events to consumer queue based on retry metadata"
    ) >> rmq_us_p
    retry_p >> Edge(
        label="After x amount of retries, move events to DLQ"
    ) >> deadletter_queue
    deadletter_queue << Kafka("connect") >> S3("crm-data-import-live")
