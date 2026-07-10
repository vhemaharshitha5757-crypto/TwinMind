from neo4j import GraphDatabase


class Neo4jService:

    def __init__(
        self,
        uri="bolt://127.0.0.1:7687",
        user="neo4j",
        password="password"
    ):
        self.driver = GraphDatabase.driver(
            uri,
            auth=(user, password)
        )

    def close(self):
        self.driver.close()

    # -----------------------------
    # Create Node
    # -----------------------------
    def create_node(self, label, name):

        query = f"""
        MERGE (n:{label} {{name:$name}})
        """

        with self.driver.session() as session:
            session.run(query, name=name)

    # -----------------------------
    # Create Relationship
    # -----------------------------
    def create_relation(
        self,
        source,
        target,
        source_label,
        target_label,
        relation
    ):

        query = f"""
        MATCH (a:{source_label} {{name:$source}})
        MATCH (b:{target_label} {{name:$target}})
        MERGE (a)-[:{relation}]->(b)
        """

        with self.driver.session() as session:
            session.run(
                query,
                source=source,
                target=target
            )

    # -----------------------------
    # Store Whole Graph
    # -----------------------------
    def store_graph(self, graph):

        # Create Nodes
        for node in graph.nodes:
            self.create_node(
                node.label,
                node.name
            )

        # Create Relations
        for rel in graph.relations:

            source_label = "Incident"

            target_label = None

            for node in graph.nodes:
                if node.name == rel.target:
                    target_label = node.label
                    break

            if target_label is None:
                continue

            self.create_relation(
                rel.source,
                rel.target,
                source_label,
                target_label,
                rel.relation
            )

        print("✅ Graph stored successfully in Neo4j")
