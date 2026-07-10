from models.graph_models import (
    GraphData,
    GraphNode,
    GraphRelation
)


class GraphBuilder:

    def build(self, incident):

        graph = GraphData()

        # ---------------- Incident ----------------

        graph.nodes.append(
            GraphNode(
                label="Incident",
                name=incident.incident_id
            )
        )

        # ---------------- Systems ----------------

        for system in incident.systems:

            graph.nodes.append(GraphNode(label="System", name=system))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=system,
                    relation="AFFECTS"
                )
            )

        # ---------------- Components ----------------

        for component in incident.components:

            graph.nodes.append(GraphNode(label="Component", name=component))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=component,
                    relation="HAS_COMPONENT"
                )
            )

        # ---------------- Engineers ----------------

        for engineer in incident.engineers:

            graph.nodes.append(GraphNode(label="Engineer", name=engineer))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=engineer,
                    relation="ASSIGNED_TO"
                )
            )

        # ---------------- Departments ----------------

        for dept in incident.departments:

            graph.nodes.append(GraphNode(label="Department", name=dept))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=dept,
                    relation="BELONGS_TO"
                )
            )

        # ---------------- Locations ----------------

        for location in incident.locations:

            graph.nodes.append(GraphNode(label="Location", name=location))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=location,
                    relation="OCCURRED_AT"
                )
            )

        # ---------------- Symptoms ----------------

        for symptom in incident.symptoms:

            graph.nodes.append(GraphNode(label="Symptom", name=symptom))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=symptom,
                    relation="HAS_SYMPTOM"
                )
            )

        # ---------------- Root Cause ----------------

        for cause in incident.root_causes:

            graph.nodes.append(GraphNode(label="RootCause", name=cause))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=cause,
                    relation="CAUSED_BY"
                )
            )

        # ---------------- Resolution ----------------

        for resolution in incident.resolutions:

            graph.nodes.append(GraphNode(label="Resolution", name=resolution))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=resolution,
                    relation="RESOLVED_BY"
                )
            )

        # ---------------- SOP ----------------

        for sop in incident.sops:

            graph.nodes.append(GraphNode(label="SOP", name=sop))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=sop,
                    relation="FOLLOWS"
                )
            )

        # ---------------- Timeline ----------------

        for event in incident.timeline:

            graph.nodes.append(GraphNode(label="TimelineEvent", name=event))

            graph.relations.append(
                GraphRelation(
                    source=incident.incident_id,
                    target=event,
                    relation="HAS_EVENT"
                )
            )

        return graph
