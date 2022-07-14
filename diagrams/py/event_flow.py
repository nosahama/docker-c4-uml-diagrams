from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.k8s.compute import Pod
from icons import RMQ_ICON, SALESFORCE_ICON

with Diagram(
    "Transactional Communication Service Consumers RMQ Events Flow",
    filename="event_flow",
    show=False,
):

    with Cluster("Gateway Consumer RMQ queues"):
        rmq_us_g = Custom("tcs-gateway.us \n [us.transactional.event.send]", RMQ_ICON)
        rmq_dach_g = Custom(
            "tcs-gateway.dach \n [{de | at | ch}.transactional.event.send]", RMQ_ICON
        )
        rmq_anon_g = Custom(
            "tcs-gateway.{business_unit} \n [{business_unit}.transactional.event.send]",
            RMQ_ICON,
        )

    with Cluster("Gateway Consumer Pods"):
        us_gc = Pod("consumer-gateway-us")
        dach_gc = Pod("consumer-gateway-dach")
        anon_gc = Pod("consumer-gateway-{business_unit}")

    with Cluster("Provider Consumer RMQ queues"):
        rmq_us_p = Custom(
            "tcs-salesforce.us \n [us.transactional.salesforce.send]", RMQ_ICON
        )
        rmq_dach_p = Custom(
            "tcs-salesforce.dach \n [{de | at | ch}.transactional.salesforce.send]",
            RMQ_ICON,
        )
        rmq_anon_p = Custom(
            "tcs-{provider}.{business_unit} \n [{business_unit}.transactional.salesforce.send]",
            RMQ_ICON,
        )

    with Cluster("Provider Consumer Pods"):
        us_pc = Pod("consumer-salesforce-us \n transactional & behavioural")
        dach_pc = Pod("consumer-salesforce-dach  \n transactional & behavioural")
        anon_pc = Pod(
            "consumer-{provider}-{business_unit}  \n transactional & behavioural"
        )

    exchange = Custom("RMQ Exchanges \n [type: tcs.event.send]", RMQ_ICON)
    salesforce = Custom("Salesforce", SALESFORCE_ICON)

    exchange >> rmq_us_g
    exchange >> rmq_dach_g
    exchange >> rmq_anon_g
    rmq_us_g << us_gc
    rmq_dach_g << dach_gc
    rmq_anon_g << anon_gc
    us_gc >> rmq_us_p
    dach_gc >> rmq_dach_p
    anon_gc >> rmq_anon_p
    rmq_us_p << us_pc
    rmq_dach_p << dach_pc
    rmq_anon_p << anon_pc
    us_pc >> salesforce
    dach_pc >> salesforce
    anon_pc >> salesforce
