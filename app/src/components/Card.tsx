import { FunctionComponent } from "react";

type Props = {
  className?: string;
};

const Card: FunctionComponent<Props> = ({ className = "", children }) => {
  return (
    <div className={`p-6 sm:p-8 md:p-10 shadow-custom rounded-lg ${className}`}>{children}</div>
  );
};

export default Card;