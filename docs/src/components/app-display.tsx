import ReactFlow, { Background, Controls, MiniMap } from "reactflow";
import "reactflow/dist/style.css";
import nodeTypes from "./nodes/nodeTypes";
import { Download } from "lucide-react";

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

  const download = () => {
    const jsonString = JSON.stringify(app, null, 2);
    const blob = new Blob([jsonString], { type: "application/json" });

    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "app.json";
    a.click();

    URL.revokeObjectURL(url);
  };

  return (
    <div className="mt-6">
      <div className="flex items-center">
        <h4>Example app</h4>
        <Download onClick={download} className="ml-2 cursor-pointer !mt-1" />
      </div>
      <div>
        <div className="flex justify-center">
          <div style={{ width: "100vw", height: 400 }} className="not-content">
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
      </div>
    </div>
  );
};

export default AppDisplay;
