import { ConfigProvider, Input } from "antd";
const { Search } = Input;

const SearchBox: React.FC<{ onQuery: any }> = ({ onQuery }) => {
    return (
        <div className="h-[10%] w-1/2 bg-[#212121] fixed bottom-0">
            <ConfigProvider
                theme={{
                    token: {
                        colorBgContainer: "#2f2f2f",
                        colorBorder: "#2f2f2f",
                        colorText: "#ffffff",
                        colorPrimaryActive: "#2f2f2f",
                        colorPrimary: "#2f2f2f",
                        colorTextPlaceholder: "#676767",
                        colorIcon: "#ffffff",
                        colorIconHover: "#ffffff",
                    },
                }}
            >
                <Search
                    placeholder="Input search text"
                    allowClear
                    onSearch={onQuery}
                    className="w-full rounded-full"
                    size="large"
                />
            </ConfigProvider>
        </div>
    );
};

export default SearchBox;
