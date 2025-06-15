import { ThreeDots } from "react-loader-spinner";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGhost } from "@fortawesome/free-solid-svg-icons";
import { useRef, useEffect } from "react";
const Chat: React.FC<{ currentSession: any; loading: any }> = ({ currentSession, loading }) => {
    const myDivRef = useRef<HTMLDivElement | null>(null);

    const scrollToDiv = () => {
        if (myDivRef.current) {
            myDivRef.current.scrollIntoView({ behavior: "smooth" });
        }
    };

    // Scroll to the empty div at the end of the chat display
    useEffect(() => {
        scrollToDiv();
    }, [currentSession, loading]);

    if (currentSession) {
        const currentHistory = currentSession["history"];
        if (currentHistory.length === 0) {
            return (
                <div className="text-white text-4xl">
                    <span>Enter something</span>
                </div>
            );
        }
        return (
            <div className="h-[85%] w-full flex items-center flex-col overflow-y-scroll overflow-x-hidden scrollbar">
                {currentHistory.map((item: any, idx: any) => {
                    if (idx % 2 === 0) {
                        // Display user query
                        return (
                            <div key={idx} className="w-1/2 my-4 flex justify-end">
                                <p className="p-2 w-[500px] text-left border-2 border-stone-400 rounded-xl text-white">
                                    {item}
                                </p>
                            </div>
                        );
                    } else {
                        // Display LLM response
                        return (
                            <div key={idx} className="w-1/2 my-4 flex justify-start">
                                <FontAwesomeIcon
                                    className="text-3xl mr-2 text-white"
                                    icon={faGhost}
                                />
                                <p className="p-2 w-[500px] text-left border-2 border-stone-400 rounded-xl text-white whitespace-pre-line">
                                    {item}
                                </p>
                            </div>
                        );
                    }
                })}

                {/* Loading animation while waiting for response*/}
                {loading && (
                    <div className="w-full mt-8 ml-[850px] flex">
                        <ThreeDots
                            visible={true}
                            height="30"
                            width="30"
                            color="#ffffff"
                            radius="5"
                            ariaLabel="three-dots-loading"
                            wrapperStyle={{}}
                            wrapperClass=""
                        />
                    </div>
                )}

                {/* Empty element */}
                <div ref={myDivRef}></div>
            </div>
        );
    }
};
export default Chat;
