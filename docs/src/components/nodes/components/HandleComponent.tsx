import { type CustomNodeProps } from "../types/nodeProps";
import { Position } from "reactflow";
import { CustomHandle, type HandleVariantProps } from "./CustomHandle";

const HandleComponent = ({
  data,
  variant,
}: {
  data: CustomNodeProps["data"];
} & HandleVariantProps) => {
  const outputs = data.outputs ?? [];
  const inputs = data.inputs ?? [];

  return (
    <>
      <div className="!m-0 absolute -left-1 top-0 flex h-full flex-col justify-evenly">
        {inputs.map((param) => (
          <div
            className="relative flex items-center"
            key={`input-${data.id}-${param.name}`}
          >
            <CustomHandle
              className="!m-0 left-0"
              position={Position.Left}
              type="target"
              param={param}
              variant={variant}
            />
          </div>
        ))}
      </div>

      <div className="!m-0 absolute -right-1 top-0 flex h-full flex-col justify-evenly">
        {outputs.map((param) => (
          <div
            className="relative flex items-center"
            key={`input-${data.id}-${param.name}`}
          >
            <CustomHandle
              className="!m-0 right-0"
              position={Position.Right}
              type="source"
              param={param}
              variant={variant}
            />
          </div>
        ))}
      </div>
    </>
  );
};

export default HandleComponent;
