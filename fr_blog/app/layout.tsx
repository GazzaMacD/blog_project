type TRootLayoutProps = {
    children: React.ReactNode;
};

function RootLayout({ children }: TRootLayoutProps) {
    return (
        <html>
            <head></head>
            <body>
                <header>Logo + some navigation</header>
                {children}
            </body>
        </html>
    );
}
export default RootLayout;
