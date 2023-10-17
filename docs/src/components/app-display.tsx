import ReactFlow, { Background, Controls, MiniMap } from "reactflow";
import "reactflow/dist/style.css";
import nodeTypes from "./nodes/nodeTypes";

type AppDisplayProps = {
  app: any;
};

const FlowMiniMap = () => {
  return (
    <MiniMap
      style={{
        backgroundColor: "rgba(255, 255, 255, 0.1)",
        height: 80,
        width: 150,
      }}
      nodeColor="rgba(255, 255, 255, 0.25)"
      maskColor="rgba(255, 255, 255, 0.05)"
      zoomable
      pannable
    />
  );
};

const AppDisplay = ({ app }: AppDisplayProps) => {
  const appObject = app["rfInstance"];
  const nodes = appObject["nodes"];
  const edges = appObject["edges"];

  return (
    <div className="flex justify-center">
      <div style={{ width: 500, height: 400 }} className="not-content">
        <ReactFlow
          nodes={nodes}
          nodeTypes={nodeTypes}
          edges={edges}
          minZoom={0.25}
          fitView
          proOptions={{ hideAttribution: true }}
        >
          <FlowMiniMap />
          <Background />
          <Controls />
        </ReactFlow>
      </div>
    </div>
  );
};

export default AppDisplay;
