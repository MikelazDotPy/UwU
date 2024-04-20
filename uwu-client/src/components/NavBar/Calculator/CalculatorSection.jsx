import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCalculator} from "@fortawesome/free-solid-svg-icons";
import {useState} from "react";

const CalculatorSection = ({}) => {

    const [show, setShow] = useState(false);

    return (
        <>
            <div className="flex mt-3 space-x-10 align-middle">
                <FontAwesomeIcon icon={faCalculator} className="text-overall-purple text-[20px] ml-[5px] mt-2"/>
                <h2 className="text-[24px] text-overall-purple"
                    onClick={() => {
                        setShow(!show)
                    }}
                >Калькулятор</h2>
            </div>
            {show && <div className="ml-5 mt-2">
                <div className="text-[14px] text-gray-500">Данные для поступления</div>
                
            </div>}
        </>
    )
}

export default CalculatorSection