"""Chạy thư viện async (gemini-webapi) từ code đồng bộ: một event loop riêng chạy ở luồng nền."""

from __future__ import annotations

import asyncio
import queue
import threading
from typing import Any, AsyncIterator, Awaitable, Iterator


class BackgroundLoop:
    def __init__(self) -> None:
        self._loop = asyncio.new_event_loop()
        threading.Thread(target=self._loop.run_forever, daemon=True, name="aio-loop").start()

    def run(self, coro: Awaitable[Any], timeout: float | None = None) -> Any:
        return asyncio.run_coroutine_threadsafe(coro, self._loop).result(timeout)

    def iterate(self, agen: AsyncIterator[Any]) -> Iterator[Any]:
        """Biến async generator thành iterator thường; lỗi bên trong được ném lại cho bên gọi."""
        q: queue.Queue = queue.Queue()

        async def pump() -> None:
            try:
                async for item in agen:
                    q.put(("item", item))
            except BaseException as e:   # noqa: BLE001 - chuyển mọi lỗi sang luồng gọi
                q.put(("error", e))
            else:
                q.put(("end", None))

        fut = asyncio.run_coroutine_threadsafe(pump(), self._loop)
        try:
            while True:
                kind, value = q.get()
                if kind == "item":
                    yield value
                elif kind == "error":
                    raise value
                else:
                    return
        finally:
            fut.cancel()   # bên gọi dừng sớm → hủy luôn request đang chạy
