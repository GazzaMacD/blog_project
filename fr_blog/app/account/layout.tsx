function DashboardLayout({ children }: { children: React.ReactNode }) {
    return (
        <>
            <aside>
                <ul>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </aside>
            <main>{children}</main>
        </>
    );
}
export default DashboardLayout;
