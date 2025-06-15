import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSquarePlus, faTrashCan, faBars } from "@fortawesome/free-solid-svg-icons";

import React, { useState, useEffect } from "react";
import { EllipsisOutlined } from "@ant-design/icons";
import { Dropdown } from "antd";

const Session: React.FC<{
    allSessions: Array<SessionDataType>;
    currentSession: SessionDataType | null;
    handleChangeSession: any;
    handleCreateSession: any;
    handleDeleteSession: any;
}> = ({
    allSessions,
    currentSession,
    handleChangeSession,
    handleCreateSession,
    handleDeleteSession,
}) => {
    const [selectedIndex, setSelectedIndex] = useState<number | null>(null);
    useEffect(() => {
        if (selectedIndex !== null && !allSessions[selectedIndex]) {
            setSelectedIndex(null); // Reset the index if the session no longer exists
        }
    }, [allSessions, selectedIndex]);

    return (
        <div className="w-1/5">
            {/* Header */}
            <div
                className="h-12 text-4xl text-white font-mono flex justify-around items-center bg-[#171717]"
                style={{ height: "10vh" }}
            >
                <p>TITLE</p>
                <FontAwesomeIcon
                    className="text-3xl mr-2 text-white active:text-cyan-600"
                    icon={faSquarePlus}
                    onClick={() => handleCreateSession()}
                />
            </div>

            {/* Render all sessions */}
            <div
                className="w-full flex flex-col pl-4 pt-4 overflow-y-scroll bg-[#171717]  
                scrollbar"
                style={{ height: "90vh" }}
            >
                {allSessions.map((item: SessionDataType, idx: number) => {
                    // Define className and active class
                    let itemClassName =
                        "text-white flex pl-4 w-[95%] h-10 rounded-lg active:bg-stone-800 hover:bg-[#212121] border-white";
                    if (currentSession && item["_id"] === currentSession["_id"]) {
                        itemClassName += " bg-[#212121]";
                    }

                    // Render items
                    return (
                        <div
                            className={"flex relative items-center " + itemClassName}
                            key={idx}
                            onClick={() => {
                                handleChangeSession(idx);
                                setSelectedIndex(idx);
                            }}
                        >
                            {/* Render title */}
                            <p>{item["_id"].slice(0, 5)}</p>

                            {/* Render menu for each item */}
                            {selectedIndex == idx && (
                                <div className="absolute right-5">
                                    <Dropdown
                                        trigger={["click"]}
                                        placement="bottomLeft"
                                        dropdownRender={() => (
                                            <div className="flex flex-col bg-[#2f2f2f] w-32 rounded-xl">
                                                {/* Delete button */}
                                                <div
                                                    className="flex items-center font-medium text-red-700 hover:bg-stone-700 h-10 rounded-t-xl"
                                                    onClick={async () => {
                                                        await handleDeleteSession(item["_id"]);
                                                        setSelectedIndex(null);
                                                    }}
                                                >
                                                    <FontAwesomeIcon
                                                        className="text-xl text-red-700 mx-4"
                                                        icon={faTrashCan}
                                                    />
                                                    <span>Delete</span>
                                                </div>
                                                <div
                                                    className="flex items-center font-medium text-white hover:bg-stone-700 h-10x"
                                                    onClick={() => {}}
                                                >
                                                    <FontAwesomeIcon
                                                        className="text-xl text-whitie mx-4"
                                                        icon={faBars}
                                                    />
                                                    <span>Option 2</span>
                                                </div>
                                                <div
                                                    className="flex items-center font-medium text-white hover:bg-stone-700 h-10 rounded-b-xl"
                                                    onClick={() => {}}
                                                >
                                                    <FontAwesomeIcon
                                                        className="text-xl text-whitie mx-4"
                                                        icon={faBars}
                                                    />
                                                    <span>Option 3</span>
                                                </div>
                                            </div>
                                        )}
                                    >
                                        {/* Collapse icon */}
                                        <button onClick={(e) => e.preventDefault()}>
                                            <EllipsisOutlined className="text-stone-300 text-3xl hover:text-white" />
                                        </button>
                                    </Dropdown>
                                </div>
                            )}
                        </div>
                    );
                })}
            </div>
        </div>
    );
};

export default Session;
