import "./index.css";
import { Input } from "antd";
import type { GetProps } from "antd";
type SearchProps = GetProps<typeof Input.Search>;
import React, { useState, useEffect } from "react";

import Chat from "./components/Chat";
import Session from "./components/Session";
import SearchBox from "./components/SearchBox";

import { search } from "./api/query/function";
import { getAllSession, updateSession, createSession, deleteSession } from "./api/session/function";

const App: React.FC = () => {
    const [toggle, setToggle] = useState(false);
    const [loading, setLoading] = useState(false);
    const [allSessions, setAllSessions] = useState<SessionDataType[]>([]);
    const [currentSession, setCurrentSession] = useState<SessionDataType | null>(null);
    const [currentUserID, setCurrentUserID] = useState("81f42912-376d-4f67-a71f-19676ca421e4");

    const onQuery: SearchProps["onSearch"] = async (value: string, _e: any) => {
        if (value !== "") {
            // Update the current session's history for displaying
            setCurrentSession((prevCurrentSession: any) => {
                return {
                    ...prevCurrentSession,
                    history: [...prevCurrentSession["history"], value],
                };
            });
            setToggle((prevState) => !prevState);
            await onResponse(value); // Query
        }
    };

    // Update the current session's history
    const handleUpdateSesssion = async (id: string, history: Array<string>) => {
        if (currentSession) {
            await updateSession(id, history);
        }
    };

    // Change the current session
    const handleChangeSession = (idx: number) => {
        setCurrentSession(allSessions[idx]);
    };

    // Create new session
    const handleCreateSession = async () => {
        const response = await createSession(currentUserID);
        const new_session = response.data.data;
        setCurrentSession(new_session);
        setAllSessions((prevAllSession) => [...prevAllSession, new_session]);
    };

    const handleDeleteSession = async (delete_session_id: string) => {
        await deleteSession(delete_session_id);
        setCurrentSession(null);
        setAllSessions((prevAllSession: Array<SessionDataType>) => {
            return prevAllSession.filter((item) => item["_id"] !== delete_session_id);
        });
    };

    // Delay the loading animation
    const handleDelayLoading = () => {
        setTimeout(() => {
            setLoading(true);
        }, 250);
    };

    const onResponse = async (searchText: string) => {
        handleDelayLoading();
        const res = await search(searchText); // Call API
        console.log(res.data.data);
        // Update session's history in the db
        if (currentSession) {
            handleUpdateSesssion(currentSession["_id"], [
                ...currentSession["history"],
                searchText,
                res.data.data,
            ]);
        }

        // Update the current session's history for displaying
        setCurrentSession((prevCurrentSession: any) => {
            return {
                ...prevCurrentSession,
                history: [...prevCurrentSession["history"], res.data.data],
            };
        });
        setToggle((prevState) => !prevState);
        setLoading(false);
    };

    // Fetch all session data
    useEffect(() => {
        const loadData = async () => {
            const res = await getAllSession();
            setAllSessions(res);
        };
        loadData();
    }, [toggle]);

    return (
        <div className="flex w-full h-full flex-row">
            <Session
                allSessions={allSessions}
                currentSession={currentSession}
                handleChangeSession={handleChangeSession}
                handleCreateSession={handleCreateSession}
                handleDeleteSession={handleDeleteSession}
            />

            <div className="h-screen w-full flex items-center flex-col bg-[#212121]">
                {/* Chat History */}
                <Chat currentSession={currentSession} loading={loading} />

                {/* Search box */}
                <SearchBox onQuery={onQuery} />
            </div>
        </div>
    );
};

export default App;
